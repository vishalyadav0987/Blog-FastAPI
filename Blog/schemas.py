from pydantic import BaseModel
from typing import List


class Blog(BaseModel):
    title:str
    content:str


class ResponseModelUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog]
    class Config():
        from_attributes = True



class ResponseModel(BaseModel):
    title:str
    content:str
    user:ResponseModelUser
    class Config():
        from_attributes = True


class User(BaseModel):
    name:str
    email:str
    password:str







# Note:
#   class Config():
#         orm_mode = True 
# Why i am using Config class ?
# because i am using Sqlalchemy query for fetching,delete,update the data from database
# basically the CRUD operation