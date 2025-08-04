import json
from tools.granite import granite_prompt

def safe_json_parse(response):
    try:
        json_array_start = response.find('{')
        if json_array_start == -1:
            raise ValueError("No JSON array found.")
        cleaned = response[json_array_start:]
        json_array_end = cleaned.rfind('}')
        if json_array_end != -1:
            cleaned = cleaned[:json_array_end + 1]
        return json.loads(cleaned)
    except Exception as e:
        print(f"[ERROR] Failed to parse JSON: {e}")
        print(f"[RAW OUTPUT]\n{response}")
        return None

def reflect_on_output(step: str, result):
    prompt = f"""
        You are an autonomous AI agent.

        You just completed the following step:
        "{step}"

        Here is the result:
        \"\"\"{str(result)}\"\"\"

        Was this step successful?

        Return ONLY a JSON object in one of these formats:
        {{"success": true}} 
        OR 
        {{"success": false, "reason": "<short reason>"}}

        Do NOT include any commentary, preamble, explanation, or Markdown.
    """

    response = granite_prompt(prompt).strip()

    try:
        cleaned = safe_json_parse(response)
        return cleaned
    except Exception as e:
        print(f"[ERROR] Reflection parse error: {e}")
        print(f"[RAW REFLECTION OUTPUT]\n{response}")
        return {"success": False, "reason": "Could not parse reflection."}
