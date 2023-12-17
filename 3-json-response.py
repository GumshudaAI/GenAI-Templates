import openai
client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "user", "content":"Which language is best for C++ programming, json"}
    ],
    response_format={"type": "json_object"}
)

print(response.choices[0].message.content)