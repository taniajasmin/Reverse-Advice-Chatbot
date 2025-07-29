import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_bad_advice(question):
    prompt = (
        f"You are a mischievous AI that gives the worst possible advice to any question. "
        f"Be sarcastic, funny, or ridiculous — but keep it short.\n\n"
        f"Q: {question}\n"
        f"A:"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you're using GPT-4
            messages=[{"role": "user", "content": prompt}],
            temperature=0.95,
            max_tokens=60
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return "Oops, the chaos machine is broken. Try again later!"
