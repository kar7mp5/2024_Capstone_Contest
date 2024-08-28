# gpt_api.py
from dotenv import load_dotenv
import openai
import os




def gpt_api(text):
    """gpt api
    
    Args:
        text (str): input text
    """
    load_dotenv()

    openai.api_key = os.getenv("GPT_API")

    messages = [ {"role": "system",
                "content": "You are a intelligent assistant by korean."} ]

    messages.append(
        {"role": "user", "content": text},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

    return messages




if __name__=="__main__":
    gpt_api('안녕')