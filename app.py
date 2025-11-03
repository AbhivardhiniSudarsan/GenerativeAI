import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from newspaper import Article
from lxml import html

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash")

#streamlit app setup
st.set_page_config(page_title="AI News Summarizer", page_icon="📰", layout="centered")
st.title("AI News Summarizer")
st.markdown("Paste a news article URL below and let Gemini summarize it for you.")


#Input
url = st.text_input("🔗 Enter a news article link:")

if st.button("Summarize"):
    if not url:
        st.warning("Please enter a valid URL.")
    else:
        try:
            with st.spinner("Fetching article..."):
                article = Article(url)
                article.download()
                article.parse()

            with st.spinner("Summarizing with Gemini..."):
                prompt = f"Summarize the following article in 5 bullet points:\n\n{article.text}"
                response = model.generate_content(prompt)
                summary = response.text

            st.success("✅ Summary generated successfully!")
            st.subheader("🧩 Summary:")
            st.write(summary)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")