import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = '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'

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
print(response)