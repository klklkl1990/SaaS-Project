import os
import openai
from consts import *
# Load your API key from an environment variable or secret management service
openai.api_key = OPEN_AI_KEY

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
print(response)