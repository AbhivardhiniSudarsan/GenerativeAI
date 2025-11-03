import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])

response1 = chat.send_message("Hi, can you tell me about generative AI?")
print("\nUser 1:", response1.text)

response2 = chat.send_message("Can you give me an example of how it's used in movies?")
print("\nUser 2:", response2.text)
