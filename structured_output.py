import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

article = """ In 2025, the global AI market is projected to reach $407 billion, driven by demand in 
healthcare, finance, and manufacturing. North America remains the largest contributor, 
while Asia-Pacific shows the fastest growth. Leading companies include Google, Microsoft, 
and OpenAI."""

prompt = f"""Extract the following details from this article:
1. Market size
2. Key industries
3. Leading companies
4. Fastest-growing region

Text: {article}"""

response = model.generate_content(prompt)
print("📋 Extracted Information:\n", response.text)