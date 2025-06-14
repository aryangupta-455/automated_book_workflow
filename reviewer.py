import openai
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_text(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a skilled editor improving clarity, grammar, and structure."},
            {"role": "user", "content": f"Please review and improve the following rewritten text:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content
