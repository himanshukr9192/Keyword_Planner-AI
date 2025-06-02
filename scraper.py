import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def extract_keywords_from_url(url):
    try:
        headers = { 'User-Agent': 'Mozilla/5.0' }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        text = soup.get_text()
        words = re.findall(r'\b\w{4,}\b', text.lower())
        common_words = Counter(words).most_common(20)

        return [word for word, count in common_words]
    except Exception as e:
        return []
