from tools.granite import granite_prompt

def summarize_text(text: str):
    prompt = f"Summarize the following research abstract in simple terms:\n\n{text}\n\nSummary:"
    return granite_prompt(prompt)
