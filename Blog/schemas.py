from pydantic import BaseModel
from typing import List


class Blog(BaseModel):
    title:str
    content:str

class ResponseModelUserForFecthingBlog(BaseModel):
    name:str
    email:str
    class Config():
        from_attributes = True
class ResponseModelUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog]
    class Config():
        from_attributes = True



class ResponseModel(BaseModel):
    title:str
    content:str
    user:ResponseModelUserForFecthingBlog
    class Config():
        from_attributes = True


class User(BaseModel):
    name:str
    email:str
    password:str


class Login(BaseModel):
    username:str 
    password:str

#username as eamil

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None



# Note:
#   class Config():
#         orm_mode = True 
# Why i am using Config class ?
# because i am using Sqlalchemy query for fetching,delete,update the data from database
# basically the CRUD operation