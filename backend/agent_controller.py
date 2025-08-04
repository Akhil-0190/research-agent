import json
from tools.granite import granite_prompt
from tools.search import search_papers
from tools.summarize import summarize_text
from tools.citation import format_citations
from tools.hypothesis import generate_hypothesis
from tools.report import generate_report
from tools.reflect import reflect_on_output
from tools.rewrite import rewrite_query

MAX_RETRIES = 3

def safe_json_parse(response):
    try:
        json_array_start = response.find('[')
        if json_array_start == -1:
            raise ValueError("No JSON array found.")
        cleaned = response[json_array_start:]
        json_array_end = cleaned.rfind(']')
        if json_array_end != -1:
            cleaned = cleaned[:json_array_end + 1]
        return json.loads(cleaned)
    except Exception as e:
        print(f"[ERROR] Failed to parse JSON: {e}")
        print(f"[RAW OUTPUT]\n{response}")
        return None

class ResearchAgent:
    def __init__(self, query: str):
        self.query = query
        self.plan = []
        self.current_step = 0
        self.memory = {}
        self.thought_log = []
        self.retry_count = 0

    def think(self, message: str):
        self.thought_log.append(message)
        print(f"[THINK] {message}")

    def plan_steps(self):
        prompt = f"""
        You are a Research Agent AI.
        Your job is to break this question into 4-6 steps using available tools.

        Research question: "{self.query}"

        Tools you can use:
        - search: to find reasearch papers using arxiv
        - summarize: to condense paper content
        - citation: to generate citations
        - hypothesis: to propose new research hypotheses
        - report: to write structured, detailed and complete research reports

        Return JSON list like this:
        [
            {{"step": "Step 1: Find papers...", "tool": "search"}},
            ...
        ]

        Only return a valid JSON list. No explanation.
        """
        self.think("Generating plan with Granite...")
        response = granite_prompt(prompt)
        steps = safe_json_parse(response)

        if steps and all("step" in s and "tool" in s for s in steps):
            self.plan = steps
        else:
            self.think("❌ Failed to parse plan.")
            self.plan = []

        self.think("Plan generated.")
        return self.plan

    def reflect_success(self, step_text, result):
        reflection = reflect_on_output(step_text, result)
        try:
            data = json.loads(reflection)
            if data.get("success") is True:
                return True, "Step successful."
            elif data.get("success") is False:
                return False, data.get("reason", "Unknown reason")
        except Exception as e:
            return False, "Could not parse reflection."

    def execute_tool(self, tool):
        if tool == "search":
            improved_query = rewrite_query(self.query)
            self.memory["improved_query"] = improved_query
            print(f"🔍 Rewritten Query: {improved_query}")
            result = search_papers(improved_query)
            if not result:
                result = search_papers(self.query)
            print(result)
            self.memory["papers"] = result or []
            return result

        elif tool == "summarize":
            papers = self.memory.get("papers", [])
            if not papers:
                return None
            summaries = []
            for p in papers:
                summary = summarize_text(p.get("summary", ""))
                summaries.append(summary)
            self.memory["summaries"] = summaries
            return summaries

        elif tool == "citation":
            papers = self.memory.get("papers", [])
            if not papers:
                return None
            formatted = [format_citations(p, i + 1) for i, p in enumerate(papers)]
            self.memory["citations"] = formatted
            return formatted

        elif tool == "hypothesis":
            summaries = self.memory.get("summaries", [])
            if not summaries:
                return None
            hypothesis = generate_hypothesis(self.query, summaries)
            self.memory["hypothesis"] = hypothesis
            return hypothesis

        elif tool == "report":
            summaries = self.memory.get("summaries", [])
            hypothesis = self.memory.get("hypothesis", "")
            if not summaries or not hypothesis:
                return None
            report = generate_report(self.query, summaries, hypothesis)
            self.memory["report"] = report
            return report

        return None

    def next_action(self):
        if self.current_step >= len(self.plan):
            self.think("All steps complete.")
            return None

        step_entry = self.plan[self.current_step]
        step_text = step_entry["step"]
        tool = step_entry["tool"]

        print(f"\n🧠 STEP {self.current_step + 1}: {step_text}")
        print(f"🛠 TOOL: {tool}")

        for attempt in range(1, MAX_RETRIES + 1):
            result = self.execute_tool(tool)

            if result is None:
                self.think(f"Attempt {attempt}: Tool returned no result.")
            else:
                success, reflection = self.reflect_success(step_text, result)
                print(success, reflection)

                if success:
                    self.think(f"Step {self.current_step + 1} successful.")
                    self.memory[f"step_{self.current_step + 1}_result"] = result
                    self.retry_count = 0
                    self.current_step += 1
                    return  # ✅ Step done, move on to next step
                else:
                    self.think(f"Attempt {attempt}: Step failed — {reflection}")

            # Try again if not successful and attempts remain
            if attempt < MAX_RETRIES:
                self.think(f"Retrying step {self.current_step + 1} (attempt {attempt + 1}/{MAX_RETRIES})...")

        # ❌ All retries exhausted
        self.think(f"Step {self.current_step + 1} failed after {MAX_RETRIES} retries. Skipping.")
        self.retry_count = 0
        self.current_step += 1

    def run(self):
        self.plan_steps()
        while self.current_step < len(self.plan):
            self.next_action()
        self.think("✅ Agent run complete.")
        return self.memory
