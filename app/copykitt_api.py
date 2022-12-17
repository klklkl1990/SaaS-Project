MAX_INPUT_LENGTH=32
# uvicorn copykitt_api:app --reload
from fastapi import FastAPI, HTTPException
from copykitt import generate_snippet, generate_keywords
from mangum import Mangum

app = FastAPI()

@app.get("/generate_snippet_and_keywords")
async def generate_snippet_api(prompt: str):
    validate_api_input(prompt)
    my_snippet=generate_snippet(prompt)
    my_keyword=generate_keywords(prompt)
    return{"Snippet" : my_snippet,"Keywords" : my_keyword}

@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    validate_api_input(prompt)
    my_snippet=generate_snippet(prompt)
    return{"Snippet" : my_snippet,"Keywords" : []}


@app.get("/generate_keywords")
async def generate_snippet_api(prompt: str):
    validate_api_input(prompt)
    my_keyword=generate_keywords(prompt)
    return{"Snippet" : None,"Keywords" : my_keyword}

def validate_api_input(prompt:str):
    if len(prompt) > MAX_INPUT_LENGTH:
        raise HTTPException(status_code=400, detail=f"Input is too long. Must be under {MAX_INPUT_LENGTH} characters")