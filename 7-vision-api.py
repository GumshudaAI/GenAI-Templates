import openai
client = openai.OpenAI()

response= client.chat.completions.create(
    model="gpt-4-vision-preview", 
    messages=[
        {
            "role": "user",
            "content": {
                {"type": "text","text": "whats in this image?"},
                {
                    "type": "image_url",
                    "image_url": "insert image URL here",
                }
            }
        }
    ],
    max_tokens=300
)

print(response.choices[0].messages.content)