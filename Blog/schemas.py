from pydantic import BaseModel


class Blog(BaseModel):
    title:str
    content:str



class User(BaseModel):
    name:str
    email:str
    password:str



class ResponseModel(BaseModel):
    title:str
    content:str
    class Config():
        from_attributes = True



# Note:
#   class Config():
#         orm_mode = True 
# Why i am using Config class ?
# because i am using Sqlalchemy query for fetching,delete,update the data from database
# basically the CRUD operation