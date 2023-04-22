import requests
import json
from dotenv import load_dotenv
import os
from typing import Union

# Load the environment variables from the .env file
load_dotenv('../.env')

# Access the variables using os.environ
openai_key = os.environ.get('openai_key')

def gpt(prompt: str, max_tokens: int) -> Union[str, dict]:
    try:
        # Replace the following line with your OpenAI API key
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_key}",
        }

        data = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "temperature": 1,
            "max_tokens": max_tokens,
        }

        response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
        response.raise_for_status()
        generated_text = response.json()["choices"][0]["text"]

        return generated_text
    except Exception as error:
        return {"error": str(error)}

