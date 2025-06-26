from fastapi import FastAPI
from . import  models
from .database import engine 
from .router import blogRoutes,userRoutes

app = FastAPI()


models.Base.metadata.create_all(engine)  
# Calls the "create_all" method on the metadata object 🛠️  
# ➜ models.Base   → the Base class you made with declarative_base() 📦  
# ➜ .metadata     → holds a list of all table definitions collected from your models 📋  
# ➜ .create_all() → tells SQLAlchemy: “Yo, go check every table in that metadata” ✅  
# Pass in engine    → it uses this DB connection to actually run the CREATE TABLE commands 🔌  
# Bottom line: it auto-creates any tables that don’t already exist in the database 🏗️  
# (Won’t drop/overwrite existing ones, just fills in the missing stuff) 🤝


app.include_router(userRoutes.router)
app.include_router(blogRoutes.router)


# 6. Pydantic Model (Schema) Note: FastAPI doesn't require you to use a SQL(relational) DB] but i can use any relationalDB
# 7. Connecting to DB
# 8. Models & Tables
# 9. Exception Code & Status Code
# 10. Delete a Blog
# 11. Update a Blog
# 12. Response Model (Schema --> How i take response from API)
# Note : pydantic model ==== schemas
# Note:  SqlAlchemy Model === models
# 13. Create User 
# 14. Hashing Password
# 15. Fetch Single User
# 16. Using Docs tages
# 17. Relationship (kis user ne blog banaya hai ush user ki info ko populate karna hai)
# 18. API Router (Refactor the Code Files base)
# 19. API Router Operation (APIRouter(prefix,tags))
# 20. Login and Verify User