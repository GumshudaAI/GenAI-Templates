import openai
client = openai.OpenAI()


# Initializing the assitant
assistant = client.beta.assistants.create(
    name="OA Helper",
    instructions="You are a brillaint C++ solve who is expert at solving  \n DSA quesitons in style of codeforces and leetcode, take the question given below and solve it in C++ language",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo"
)

# Creating a Thread: is the conversation between two people
thread= client.beta.threads.create()

#Students question
message= client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need have the code for bellman ford algorithm",
)


#Initializing (Constructing) a thread
run = client. beta.threads.runs.create(
    thread_id= thread.id,
    assistant_id=assistant.id,
    instructions="Please address the student as whynesspower"
)

import time
time.sleep(20)


run_status=client.beta.threads.runs.retrieve(
     thread_id= thread.id,
     run_id= run.id
)

if run_status.status== 'completed':
    messages=client.beta.threads.messages.list(
        thread_id=thread.id,   
    )
    
    for msg in messages.data:
        role=msg.role
        content = msg.content[0].text.value
        print(f"{role.capitalize()}:{content}")

