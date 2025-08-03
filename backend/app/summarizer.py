import os
import re
from dotenv import load_dotenv
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

load_dotenv()

def summarize_abstract(abstract: str) -> str:
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

    prompt = (
        f"Summarize the following scientific abstract in 3 concise bullet points:\n\n{abstract}"
    )

    try:
        response = model.generate_text(
            prompt=prompt,
            params={
                "decoding_method": "sample",
                "top_p": 0.9,              # balance quality & creativity
                "temperature": 0.65,       # lower = more focused, academic tone
                "max_new_tokens": 200
            }
        )
        return re.sub(r'^["\'\n\r\s]+|["\'\n\r\s]+$', '', response)
    except Exception as e:
        return f"[Granite summarization failed] {str(e)}"

def generate_hypothesis(all_summaries: list, topic: str) -> str:
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

    combined = "\n\n".join(all_summaries[:5])
    prompt = (
        f"Using the following research summaries on the topic '{topic}', "
        f"propose one clear, novel, and testable research hypothesis. The hypothesis should:\n"
        f"- Be grounded in gaps or opportunities highlighted in the summaries\n"
        f"- Be relevant to current scientific discourse\n"
        f"- Avoid vague or speculative claims\n\n"
        f"Summaries:\n{combined}\n\n"
        f"Proposed hypothesis:"
    )

    try:
        response = model.generate_text(
            prompt=prompt,
            params={
                "decoding_method": "sample",
                "top_p": 0.9,              # balance quality & creativity
                "temperature": 0.65,       # lower = more focused, academic tone
                "max_new_tokens": 200
            }
        )
        return re.sub(r'^["\'\n\r\s]+|["\'\n\r\s]+$', '', response)
    except Exception as e:
        return f"[Granite hypothesis generation failed] {str(e)}"