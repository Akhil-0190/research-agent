# 🧠 ResearchAgent – Autonomous AI Research Assistant

**ResearchAgent** is an AI-powered system designed to assist researchers in conducting structured academic investigations with minimal manual effort. It automates the entire research workflow — from gathering relevant papers to summarizing content, generating citations, proposing hypotheses, and drafting reports — all driven by foundation models.

> 🏆 This project is part of the **IBM SkillsBuild AICTE Internship**, supported by **Edunet Foundation**.

---

## 🚀 Key Features

- **End-to-End AI Research Pipeline**
  - Breaks down any research question into step-by-step actions.
  - Automatically selects appropriate tools for each step.

- **Agentic Intelligence**
  - Uses self-reflection to assess whether each step was successful.
  - If improvement is needed, the agent autonomously retries the task based on its own reasoning.

- **Built-in Tools**
  - 🔍 `search`: Finds relevant papers using arXiv API.
  - 📄 `summarize`: Condenses research abstracts and findings.
  - 📚 `citation`: Formats citations in APA and IEEE.
  - 💡 `hypothesis`: Proposes original research hypotheses.
  - 📝 `report`: Drafts structured research reports.
  - 🧠 `reflect`: Evaluates outcomes and guides retries.
  - 🛠 `query_rewriter`: Refines user queries for improved academic relevance.

- **Frontend Interface**
  - Accessible web UI built with FastAPI.
  - Allows users to perform search for full pipeline execution.

---

## 🛠 Tech Stack

- **Backend**: Python 3.10+, FastAPI, IBM Granite Foundation Models
- **Frontend**: React.js
- **Third-Party Services**: arXiv.org API

---

