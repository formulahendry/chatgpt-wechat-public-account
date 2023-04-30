import os
import openai
import werobot
from dotenv import load_dotenv

load_dotenv()

robot = werobot.WeRoBot(token=os.getenv("WECHAT_TOKEN"))

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt3_reply(text):
    print("Calling text-davinci-003 API...")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        max_tokens=100,
        temperature=0,
    )
    return response.choices[0].text.strip()

def get_gpt3dot5_reply(text):
    print("Calling gpt-3.5-turbo API...")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text}
        ],
        max_tokens=200,
        temperature=0.8
    )
    return response.choices[0].message.content.strip()

@robot.text
def hello_world(message):
    if (os.getenv("GPT_MODEL_VERSION") == "3"):
        reply = get_gpt3_reply(message.content)
    else:
        reply = get_gpt3dot5_reply(message.content)

    print(reply)

    return reply

robot.config['HOST'] = '0.0.0.0'
port = os.getenv("PORT")
robot.config['PORT'] = 8888 if port is None else port
robot.run()
