from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials
import os
from dotenv import load_dotenv
import re

load_dotenv()

def refine_query(user_query: str) -> str:
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
        f"Rewrite the following academic research question to make it more detailed, "
        f"specific, and suitable for literature search. Only return the improved question.\n\n'{user_query}'"
    )

    try:
        response = model.generate_text(
            prompt=prompt,
            params={
                "decoding_method": "greedy",
                "max_new_tokens": 100
            }
        )
        return re.sub(r'^["\'\n\r\s]+|["\'\n\r\s]+$', '', response)
    except Exception as e:
        return f"[Granite failed] {str(e)}"
