from fastapi import FastAPI
from . import schemas


app = FastAPI()



@app.post('/create-blog')
# def create_blog(title,content): # instead of paramter we use pydantic model for req.body
def create_blog(req:schemas.Blog): # instead of paramter we use pydantic model for req.body
    return {"title":req.title,"content":req.content}