import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = []

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    answer = response.choices[0].message.content

    print("Groq:", answer)

    messages.append({
        "role": "assistant",
        "content": answer
    })