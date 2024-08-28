# gpt_api.py
from dotenv import load_dotenv
import openai
import os




def gpt_api(text):
    """gpt api
    
    Args:
        text (str): input text.
        
    Returns:
        messages (str): gpt output text.
    """
    load_dotenv()

    openai.api_key = os.getenv("GPT_API")

    messages = [ 
                    {
                        "role": "system",
                        "content": """\
You are a bot programmed to respond courteously.
Based on the following content, respond with a single word for each of the five categories listed.
You only need to output the `value` corresponding to the `key` in the `json` provided.
```json
{
    "앞쪽": 1,
    "뒤쪽": 2,
    "왼쪽": 3,
    "오른쪽": 4,
    "기타": 5
}
```
Just return the value.
"""
                    } 
               ]

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
    gpt_api("안녕하세요. 반갑습니다. 우로 가라")
