import os
import re
from dotenv import load_dotenv
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

load_dotenv()

def generate_section(summaries, topic, section_type):
    api_key = os.getenv("IBM_API_KEY")
    project_id = os.getenv("WATSONX_PROJECT_ID")
    region = "eu-gb"
    url = f"https://{region}.ml.cloud.ibm.com"

    creds = Credentials(api_key=api_key, url=url)

    model = ModelInference(
        model_id="ibm/granite-3-8b-instruct",
        credentials=creds,
        project_id=project_id
    )

    # Combine summaries and lightly clean
    summary_block = "\n".join([re.sub(r'^\d+\.\s*', '', s.strip()) for s in summaries[:5]])

    # Custom prompt to enforce better structure and length
    prompt = (
        f"You are writing a scholarly paper on '{topic}'. Generate a well-structured {section_type} section "
        f"based on the following research summaries. The section should be around 500 words, written in formal academic style, "
        f"and include relevant transitions. Do not copy the summaries verbatim. End with a strong concluding sentence.\n\n"
        f"Summaries:\n{summary_block}\n\n"
        f"{section_type} Section:"
    )

    try:
        response = model.generate_text(
            prompt=prompt,
            params={
                "decoding_method": "sample",
                "top_p": 0.9,              # balance quality & creativity
                "temperature": 0.65,       # lower = more focused, academic tone
                "max_new_tokens": 1000  # Increased to avoid early cutoff
            }
        )
        return re.sub(r'^["\'\n\r\s]+|["\'\n\r\s]+$', '', response)
    except Exception as e:
        return f"[Granite {section_type.lower()} generation failed] {str(e)}"


def generate_report(topic, summaries, hypothesis):
    intro = generate_section(summaries, topic, "Introduction")
    related = generate_section(summaries, topic, "Related Work")
    conclusion = generate_section(summaries, topic, "Conclusion")

    return {
        "Introduction": intro,
        "Related Work": related,
        "Hypothesis": hypothesis.strip(),
        "Conclusion": conclusion
    }

