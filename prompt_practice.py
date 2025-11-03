import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# 1. Simple instruction
prompt1 = "Write a short paragraph explaining what prompt engineering is."
response1 = model.generate_content(prompt1)
print("\n🔹 Simple Prompt:\n", response1.text)

# 2. Role-based instruction
prompt2 = "You are a senior AI engineer. Explain prompt engineering to a 10-year-old."
response2 = model.generate_content(prompt2)
print("\n🔹 Role-based Prompt:\n", response2.text)

# 3. Format-controlled instruction
prompt3 = """
Explain prompt engineering in exactly 3 bullet points:
1. What it means
2. Why it is important
3. An example
"""
response3 = model.generate_content(prompt3)
print("\n🔹 Structured Prompt:\n", response3.text)
