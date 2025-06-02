import streamlit as st
from backend import get_keyword_suggestions, get_seo_score
from scraper import extract_keywords_from_url
from trends import get_keyword_trend
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Keyword Planner AI", layout="wide")
st.title("🔍 AI-Powered Keyword Planner")

tab1, tab2, tab3 = st.tabs(["🎯 Keyword Suggestions", "🔍 Competitor Analysis", "📈 Keyword Trends"])

with tab1:
    with st.form("keyword_form"):
        topic = st.text_input("Enter your topic or product:")
        submit = st.form_submit_button("Generate Keywords")
    
    if submit and topic:
        suggestions = get_keyword_suggestions(topic)
        st.subheader("Suggested Keywords")
        st.write(suggestions)

        st.download_button("Download Keywords", suggestions, file_name="keywords.txt")

with tab2:
    url = st.text_input("Enter competitor's URL (e.g., https://example.com):")
    if st.button("Analyze Competitor"):
        keywords = extract_keywords_from_url(url)
        st.subheader("Extracted Keywords")
        if keywords:
            st.write(keywords)
        else:
            st.warning("No keywords found or site could not be scraped.")

with tab3:
    keyword = st.text_input("Enter keyword to analyze trends:")
    if st.button("Show Trend"):
        trend_data = get_keyword_trend(keyword)
        if trend_data is not None:
            st.line_chart(trend_data)
        else:
            st.error("Could not fetch trend data.")


st.divider()
st.subheader("📊 SEO Score Estimation")
seo_text = st.text_area("Paste your content here to evaluate its SEO:")
if st.button("Estimate SEO Score"):
    score = get_seo_score(seo_text)
    st.write(score)
