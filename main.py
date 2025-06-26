from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()

# when we create file name is "main.py" and FastAPI() instance as "app" so we run the app using 
# command : uvicorn file-name:app(instance-name) --reload
# Actual Commmand: uvicorn main:app --reload like nodemon

@app.get('/blog') 
# def index(limit:int = 10, published:Optional[bool] = None, sort:Optional[str] = None):
def index(limit:int = 10, published:bool = False, sort:Optional[str] = None):
    # return a list of blogs
    # return published # without giving any data type it will take it as string
    if published:
        return {
            'data':f'{limit} published blogs from database'
        }
    else:
        return {
            'data' : f'{limit} unpublished blogs from database'
        }


@app.get('/about')
def index():
    return {
        "return Json object" : {
            'message' : 'These another route using FastApi'
        }
    }


@app.get('/contact')
def anythingnamecanbeused():
    return {
        "return Json object" : {
            'message' : 'contact page'
        }
    }

@app.get('/blog/{blogId}')
def getSingleBlog(blogId:int):
    # fetch blog with id == blogId
    return {
        'data':f'fetch single blog with id: {blogId}'
    }



@app.get('/blog/{id}/comments') # the id always be string but when except through function saying that its int
def getSingleBlog(id : int):
    # fetch blog comment with id == id
    return {
        'data':{
            f'fetch blog comments with id: {id}',
            id
        }
    }

# Creating here pydantic mode
# Schema -------
class Blog(BaseModel):
    title:str
    content:str
    published:Optional[bool]

# Schema -------


@app.post('/create-blog')
def createBlog(req:Blog): # req == request is the name of the object
    return {
        'data':{
            'blog':req,
            'message': f'Blog created successfully with title as {req.title}'
            }
        }



# This is the main function these are the entry point of the application used to run the application on the server on which it is deployed on different port
# if __name__ == '__main__':
#     uvicorn.run(app,host='127.0.0.1',port=9000);


# 1. ------> path or endpoint
# ('/')

# 2. ------> operation or method
# ('get')

# 3. ------> path operation function
# def index():
#     return {
#         "return Json object" : {
#             'message' : 'These another route using FastApi'
#         }
#     }

# 4. ------> path operation decorator
# @app.get('/')


# 1. How create Routes
# 2. Path Parameter (dynamic routes params)
# 3. API Documentation -- Swagger UI
# 4. Query Parameters (?limit=5&pages=2)
# 5. Request Body (JSON) (req.body in node.js)
# 6. Pydantic Model (Schema) Note: FastAPI doesn't require you to use a SQL(relational) DB] but i can use any relationalDB