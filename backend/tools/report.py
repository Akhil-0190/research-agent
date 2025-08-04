from tools.granite import granite_prompt

def generate_report(query: str, summaries: list, hypothesis: str):
    joined = "\n\n".join(summaries)
    
    prompt = (
        f"Given the research question:\n"
        f"{query}\n\n"
        f"Summaries of papers:\n"
        f"{joined}\n\n"
        f"Hypothesis:\n"
        f"{hypothesis}\n\n"
        f"Now draft a research report with these sections:\n"
        f"- Introduction\n"
        f"- Related Work\n"
        f"- Proposed Hypothesis\n"
        f"- Conclusion\n\n"
        f"Format it cleanly."
    )
    
    report_text = granite_prompt(prompt)

    return report_text
