from tools.granite import granite_prompt

def rewrite_query(raw_query: str) -> str:
    prompt = f"""
        You are a research assistant helping improve academic search queries.

        Here is the original query from the user:
        "{raw_query}"

        Here is the original user query:
        "{raw_query}"

        Rewrite it to be more specific, precise, and likely to return high-quality, relevant academic papers from ArXiv.
        But do ensure that the rewritten query isnt too strict, as ensuring that atleast some academic papers from ArXiv are obtained for the query remains the top priority.

        Return only the improved query, nothing else.
    """
    return granite_prompt(prompt).strip()
