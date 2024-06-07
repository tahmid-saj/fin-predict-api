from openai import OpenAI

from conf.openai.openai_conf import OPEN_API_KEY

openai_client = OpenAI(api_key=OPEN_API_KEY)