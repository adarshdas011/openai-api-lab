import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = chat.send_message(question)

    print("Gemini:", response.text)