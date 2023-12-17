import openai
client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content":"Which language is best for C++ programming"}
    ],
    seed=1,
)

print(response.choices[0].message.content)