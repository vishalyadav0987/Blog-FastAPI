from fastapi import FastAPI
from . import schemas


app = FastAPI()



@app.post('/create-blog')
# def create_blog(title,content): # instead of paramter we use pydantic model for req.body
def create_blog(req:schemas.Blog): # instead of paramter we use pydantic model for req.body
    return {"title":req.title,"content":req.content}





# 6. Pydantic Model (Schema) Note: FastAPI doesn't require you to use a SQL(relational) DB] but i can use any relationalDB
# 7. Connecting to DB