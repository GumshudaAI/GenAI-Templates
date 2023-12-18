import openai
client = openai.OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="a cool mobile wallpaper of might guy from Naruto",
    size="1024x1024",
    quality="standard",
    n=1
)
image_url=response.data[0].url

print(image_url)