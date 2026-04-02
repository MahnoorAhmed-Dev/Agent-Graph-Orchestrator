import os
from dotenv import load_dotenv

load_dotenv()

PROVIDERS = {
  "default" : {
    
    "api_key": os.getenv("GROQ_API_KEY"),
    "base_url": os.getenv("GROQ_BASE_URL"),
    "model": os.getenv("GROQ_MODEL")
}
}

TEMPERATURE =float(os.getenv("TEMPERATURE", 0.7))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 100))