import openai
import cv2
import base64
client = openai.OpenAI()

#The video is in the same directory as this file
# hence writing just the name
video = cv2.VideoCapture("video.mp4")

# Converting video to base64 encoded frames, stored in the array
base64Frames= []
while video.isOpened():
    success, frame = video.read()
    if not success:
        break
    _, buffer = cv2.imencode(".jpg", frame)
    base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

video.release()
# Processing the frames one by one
    
reponse = client.chat.completions.create(
    
    model="gpt-4-vision-preview",
    messages=[
        {
            "role":"user",
            "content":[{"image": frame} for frame in base64Frames[0:5]]
        }
    ]
       
)

# Description of the whole video
print(reponse.choices[0].message.content)