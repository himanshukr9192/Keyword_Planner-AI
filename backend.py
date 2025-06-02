import openai
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Ensure API key is set
if not api_key:
    raise ValueError("❌ API key not found! Check your .env file.")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

# Function to get keyword suggestions
def get_keyword_suggestions(topic):
    prompt = f"Suggest 10 highly effective SEO keywords or phrases for: {topic}.\nReturn them as a bullet list."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()

    except openai.RateLimitError:
        print("⚠️ Rate limit exceeded! Waiting before retrying...")
        time.sleep(60)  
        return get_keyword_suggestions(topic)

# Function to evaluate SEO score
def get_seo_score(text):
    prompt = f"Evaluate the SEO quality of the following content. Give a score out of 100 and explain strengths and weaknesses:\n\n{text}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()

    except openai.RateLimitError:
        print("⚠️ Rate limit exceeded! Waiting before retrying...")
        time.sleep(60)
        return get_seo_score(text)
