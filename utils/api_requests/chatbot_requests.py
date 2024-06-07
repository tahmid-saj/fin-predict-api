from services.openai.openai import openai_client
from conf.openai.openai_conf import OPEN_API_MODEL, OPEN_API_ROLE

import os
from dotenv import load_dotenv

load_dotenv()

def request_chatbot(request):
  chat_completion = openai_client.chat.completions.create(
    model=OPEN_API_MODEL,
    messages=[
      {
        "role": OPEN_API_ROLE,
        "content": str(request)
      }
    ]
  )
  
  response = chat_completion.choices[0].message.content
  
  return str(response)