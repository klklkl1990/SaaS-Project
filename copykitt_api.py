
# uvicorn copykitt_api:app --reload
from fastapi import FastAPI
from copykitt import generate_snippet, generate_keywords

app = FastAPI()


@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    my_snippet=generate_snippet(prompt)
    return{f"Snippet: {my_snippet}"}


@app.get("/generate_keywords")
async def generate_snippet_api(prompt: str):
    my_keyword=generate_keywords(prompt)
    return{"Keywords" : my_keyword}