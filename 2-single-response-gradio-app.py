import openai
import gradio as gr
client = openai.OpenAI()

def get_openai_response(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content":question}
        ]
    )
    return response.choices[0].message.content

iface= gr.Interface(fn=get_openai_response, inputs="text", outputs="text")
iface.launch()
