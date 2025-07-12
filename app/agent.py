from openai import OpenAI
from app.context_loader import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_openai(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful and reflective assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
