from config.settings import PROVIDERS, TEMPERATURE, MAX_TOKENS
from app.llm.client import LLMClient

client = LLMClient(
  config=PROVIDERS["default"],
  temperature=TEMPERATURE,
  max_tokens=MAX_TOKENS
)

print(client.chat("Explain graph-based agent orchestration?"))