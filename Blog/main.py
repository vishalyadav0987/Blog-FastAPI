from fastapi import FastAPI,Depends,HTTPException,status
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



@app.post('/create-blog',status_code=status.HTTP_201_CREATED)
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



@app.get('/blog',status_code=status.HTTP_200_OK)
def get_all_blog(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs




@app.get('/blog/{blogId}',status_code=status.HTTP_200_OK)
def get_single_blog(blogId:int,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blogId).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    return blog
# we use here "HTTPException" because we want to return 404 status code




@app.delete('/delete-blog',status_code=status.HTTP_200_OK)
def delete_blog(blogId:int,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blogId).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    db.query(models.Blog).filter(models.Blog.id == blogId).delete(synchronize_session=False)
    db.commit()
    return {"message":"Blog deleted successfully"} 
# we use here "HTTPException" because we want to return 404 status code
# we use here "synchronize_session=False" because we want to delete the blog from database
# and we don't want to update the session
# 1️⃣  Session खोलो
# 2️⃣  मान लो पहले कुछ users बनाकर commit कर चुके हो…
# 3️⃣  अब user id == 5 डिलीट करना है
# 4️⃣  user id == 5 को delete करो
# 5️⃣  जहाँ id 5 है
# 6️⃣  DELETE statement रन करो
# 7️⃣  session को अभी न छेड़ो
# 8️⃣  matlab ye hai ki session ko abhi kuch mat kar phle jo dlete kra usko commit kro aur refresh kar do takki session up to date ho jaye



# 6. Pydantic Model (Schema) Note: FastAPI doesn't require you to use a SQL(relational) DB] but i can use any relationalDB
# 7. Connecting to DB
# 8. Models & Tables
# 9. Exception Code & Status Code
# 10. Delete a Blog