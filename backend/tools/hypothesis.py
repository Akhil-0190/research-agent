from tools.granite import granite_prompt

def generate_hypothesis(query: str, summaries: list):
    combined = "\n\n".join(summaries[:3])
    prompt = (
        f"A researcher asked: {query}\n"
        f"Below are summaries of relevant research papers:\n"
        f"{combined}\n\n"
        f"Based on these, suggest a novel research hypothesis."
    )
    return granite_prompt(prompt)
