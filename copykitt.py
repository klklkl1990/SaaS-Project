import os
from typing import List
import openai
from MY_KEYS import *
import argparse
import regex as re
MAX_INPUT_LENGTH=32
MAX_TOKEN_LENGTH=32
# To run the program, we need enter the command line
# & C:/Users/Itay/AppData/Local/Programs/Python/Python38/python.exe "c:/Users/Itay/Desktop/Programming - Liad/Projects/SaaS-Project/copykitt.py"  -i "yoga mat"

#Our Main function is the entry point for our program
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--input", '-i', type=str, required= True)
    args=parser.parse_args()
    user_input=args.input
    print(f"Running CopyKitt, Generating Branding Snippet and keywords: {user_input}")

    if valid_input(user_input) is False:
        raise ValueError(f"'{user_input}' is invalid. Must be under {MAX_INPUT_LENGTH} characters")
    
    generate_snippet(user_input)
    generate_keywords(user_input)
    pass

def valid_input(prompt:str)->bool:
    return len(prompt) <15

def generate_keywords(prompt:str)->List[str]:
    openai.api_key=OPENAI_KEY
    generated_prompt=f"Generate branding keywords for {prompt}: "
    response=openai.Completion.create(model='davinci', prompt=generated_prompt, temperature=0, max_tokens=MAX_TOKEN_LENGTH)
    keywords=response['choices'][0]['text']
    #We are going to strip the keywords by using regex
    keywords=keywords.strip()
    keywords_arr=re.split(',|\n|;|-', keywords)
    keywords_arr=[keyword.lower().strip() for keyword in keywords_arr]
    keywords_arr=[keyword for keyword in keywords_arr if len(keyword) != '']
    print(f"Keywords Result: {list(enumerate(keywords_arr))}")
    return keywords_arr

def generate_snippet(prompt:str)->str:
    # Load your API key from an environment variable or secret management service
    openai.api_key = OPENAI_KEY
    generated_prompt = f"Generate upbeat branding snippet for {prompt}: "

    response = openai.Completion.create(model='text-davinci-003', prompt=generated_prompt, temperature=0, max_tokens=MAX_TOKEN_LENGTH)
    #We want to wrap our snippet, turn this into a easier interface
    #Extract the snippet from the response
    brand_snippet:str = response['choices'][0]['text']
    #strip the snippet by removing the spaces
    brand_snippet=brand_snippet.strip()
    #Add the dots to the end of the snippet
    last_dot = brand_snippet[-1]
    if last_dot != {'.','!','?'}:
        brand_snippet+='...'
    print(f"Snippet Result: {brand_snippet}")
    return brand_snippet




if __name__ == "__main__":
    main()