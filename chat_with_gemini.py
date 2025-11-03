import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
system_prompt = """
You are a helpful AI assistant specialized in healthcare.
You provide accurate, empathetic, and easy-to-understand responses to users
asking about general health, symptoms, wellness, or medical information.
You do not provide medical diagnosis, and you always suggest consulting a doctor for medical advice.
"""

model = genai.GenerativeModel(
    "gemini-2.5-flash",
     system_instruction=system_prompt
     )

print("💬 Gemini Chatbot — type 'exit' to quit")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break
    response = model.generate_content(user_input)
    print("Gemini:", response.text)
