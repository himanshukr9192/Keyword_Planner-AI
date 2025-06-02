import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # New client initialization

def get_keyword_suggestions(topic):
    prompt = f"Suggest 10 highly effective SEO keywords or phrases for the topic: {topic}.\nReturn them as a bullet list."
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

def get_seo_score(text):
    prompt = f"Evaluate the SEO quality of the following content. Give a score out of 100 and explain strengths and weaknesses:\n\n{text}"
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
