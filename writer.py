import openai
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def spin_text(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative writer rewriting classic literature for modern readers."},
            {"role": "user", "content": f"Rewrite the following text in a modern and engaging way:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content
