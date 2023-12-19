from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

def display_chat_history(messages):
    for message in messages:
        print(f"{message['role'].capitalize()}: {message['content']}")

def get_assistant_response(messages):
    r = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
    )
    response = r.choices[0].message.content
    return response

messages = [{"role": "assistant", "content": "How can I help?"}]

while True:
    display_chat_history(messages)
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    messages.append({"role": "user", "content": user_input})
    assistant_response = get_assistant_response(messages)
    messages.append({"role": "assistant", "content": assistant_response})