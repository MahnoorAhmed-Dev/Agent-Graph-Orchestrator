from openai import OpenAI


class LLMClient:
  def __init__(self, config, temperature= 0.7, max_tokens=200):
    if not config["api_key"]:
      raise ValueError("API Key Missing")
    
    self.client=OpenAI(
      api_key=config["api_key"],
      base_url=config["base_url"]
    )
    self.model=config["model"]
    self.temperature= temperature
    self.max_tokens= max_tokens

    self.messages =[
      {"role":"user", "content": "You are a helpful assistant"}
   ]
    
  def chat(self, prompt:str) -> str:
    self.messages.append({"role":"user", "content": prompt})

    response = self.client.chat.completions.create(
      model=self.model,
      messages=self.messages,
      temperature=self.temperature,
      max_tokens=self.max_tokens
    )
    reply = response.choices[0].message.content
    self.messages.append({"role": "assistant", "content": reply})

    return reply