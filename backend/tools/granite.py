import os
from dotenv import load_dotenv
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

load_dotenv()

def granite_prompt(prompt: str):
    api_key = os.getenv("IBM_API_KEY")
    project_id = os.getenv("WATSONX_PROJECT_ID")
    region = os.getenv("WATSONX_REGION", "eu-gb")  # default to eu-gb if not set
    url = f"https://{region}.ml.cloud.ibm.com"

    model_id = "ibm/granite-3-8b-instruct"  # Correct format for Watsonx SDK
    creds = Credentials(api_key=api_key, url=url)

    model = ModelInference(
        model_id=model_id,
        credentials=creds,
        project_id=project_id
    )

    response = model.generate_text(
        prompt=prompt,
        params={
            "temperature": 0.7,
            "max_new_tokens": 2048,        # Very high limit
        }
    )

    return response  # Already returns a string
