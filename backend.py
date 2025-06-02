import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_keyword_suggestions(topic):
    prompt = (
        f"Suggest 10 highly effective SEO keywords or phrases for the topic: {topic}.\n"
        f"Return them as a bullet list."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{ "role": "user", "content": prompt }],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

def get_seo_score(text):
    prompt = (
        f"Evaluate the SEO quality of the following content. "
        f"Give a score out of 100 and explain strengths and weaknesses:\n\n{text}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{ "role": "user", "content": prompt }],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
