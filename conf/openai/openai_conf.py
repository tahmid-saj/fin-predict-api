import os
from dotenv import load_dotenv

load_dotenv()

OPEN_API_KEY = os.getenv("OPEN_API_KEY")
OPEN_API_ROLE = os.getenv("OPEN_API_ROLE")
OPEN_API_MODEL = os.getenv("OPEN_API_MODEL")
