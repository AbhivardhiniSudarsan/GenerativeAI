import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Test Gemini
model = genai.GenerativeModel("gemini-2.5-flash")
prompt = "Explain what Generative AI is in simple terms."
response = model.generate_content(prompt)

print(response.text)
