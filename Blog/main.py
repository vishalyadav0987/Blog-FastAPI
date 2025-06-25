from fastapi import FastAPI,Depends
from . import schemas , models
from .database import engine ,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()


models.Base.metadata.create_all(engine)  
# Calls the "create_all" method on the metadata object 🛠️  
# ➜ models.Base   → the Base class you made with declarative_base() 📦  
# ➜ .metadata     → holds a list of all table definitions collected from your models 📋  
# ➜ .create_all() → tells SQLAlchemy: “Yo, go check every table in that metadata” ✅  
# Pass in engine    → it uses this DB connection to actually run the CREATE TABLE commands 🔌  
# Bottom line: it auto-creates any tables that don’t already exist in the database 🏗️  
# (Won’t drop/overwrite existing ones, just fills in the missing stuff) 🤝



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() # fi everthing is done



@app.post('/create-blog')
# def create_blog(title,content): # instead of paramter we use pydantic model for req.body
def create_blog(req:schemas.Blog,db:Session = Depends(get_db)): # instead of paramter we use pydantic model for req.body
    new_blog = models.Blog(title=req.title,content=req.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# when we only "db" they act like as query param but these is session type
# db:Session giving sesstion type but it "depends" on pydantics things
# we use here "depends" here because "Session" is orm part
# but we work with pydantic things



@app.get('/blog')
def get_all_blog(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# 6. Pydantic Model (Schema) Note: FastAPI doesn't require you to use a SQL(relational) DB] but i can use any relationalDB
# 7. Connecting to DB
# 8. Models & Tables