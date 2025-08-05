# 🧠 ResearchAgent – Autonomous AI Research Assistant

**ResearchAgent** is an intelligent agentic system that automates academic research workflows using foundation models. It transforms natural language queries into structured research tasks, autonomously performs each step, and self-corrects through reflection — enabling rapid, high-quality research generation with minimal manual input.

> ✅ Built as part of the **IBM SkillsBuild AICTE Internship**, powered by **Edunet Foundation** and **IBM Granite Foundation Models**.

---

## 🚀 Key Features

### 🔁 End-to-End Autonomous Pipeline
- Decomposes any research question into a multi-step plan.
- Executes tasks using specialized tools in the correct order.
- Stores and reuses memory across steps.

### 🧠 Agentic Intelligence with Self-Reflection
- Reflects after each step to determine success or failure.
- If improvement is needed, the agent retries the step automatically using its own reasoning (within safe limits).
- Ensures output quality and coherence before proceeding.

### 🧰 Modular Toolset
| Tool          | Functionality |
|---------------|---------------|
| `search`      | Fetches relevant papers from arXiv. |
| `summarize`   | Condenses research abstracts into crisp summaries. |
| `citation`    | Generates citations in both APA and IEEE styles. |
| `hypothesis`  | Proposes original research hypotheses based on literature. |
| `report`      | Drafts structured research reports with Introduction, Related Work, Hypothesis, and Conclusion. |
| `reflect`     | Evaluates whether a step was successful and guides retry logic. |
| `query_rewriter` | Refines user queries to increase academic search relevance. |

---

## 🖥 Frontend Interface

- Built using **React.js**
- Allows users to:
  - Run full research pipelines.
  - Perform targeted paper searches.
  - View citations, hypotheses, and auto-generated reports.

---

## 🛠 Tech Stack

- **Language**: Python 3.10+
- **Backend**: FastAPI, IBM Granite Foundation Model (`ibm/granite-3-8b-instruct`)
- **Frontend**: React.js (npm-based)
- **AI Services**: IBM WatsonX / IBM Cloud Lite
- **Data Source**: [arXiv.org](https://arxiv.org)

---

## 📸 Screenshots

| ![](https://github.com/Akhil-0190/research-agent/blob/main/image%201.jpg)
| ![](https://github.com/Akhil-0190/research-agent/blob/main/image%202.jpg)
| ![](https://github.com/Akhil-0190/research-agent/blob/main/image%203.jpg) 
| ![](https://github.com/Akhil-0190/research-agent/blob/main/image%204.jpg) 

---

## 🙋‍♂️ Acknowledgements

- **IBM SkillsBuild & WatsonX AI** – For providing access to Granite foundation models and cloud services.
- **Edunet Foundation** – For mentorship and internship support.
- **arXiv API** – For academic paper search and data access.
