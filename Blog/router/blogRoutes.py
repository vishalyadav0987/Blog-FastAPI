from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas
from .. import schemas , models
from ..database import get_db
from sqlalchemy.orm import Session
from .. import oauth2


router = APIRouter(
    tags=['Blogs Routes'],
    prefix='/blog',
)





@router.post('/create',status_code=status.HTTP_201_CREATED)
# def create_blog(title,content): # instead of paramter we use pydantic model for req.body
def create_blog(req:schemas.Blog,db:Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)): # instead of paramter we use pydantic model for req.body
    new_blog = models.Blog(title=req.title,content=req.content,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# when we only "db" they act like as query param but these is session type
# db:Session giving sesstion type but it "depends" on pydantics things
# we use here "depends" here because "Session" is orm part
# but we work with pydantic things



@router.get('/all',status_code=status.HTTP_200_OK,response_model=list[schemas.ResponseModel])
def get_all_blog(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs




@router.get('/{blogId}',status_code=status.HTTP_200_OK,response_model=schemas.ResponseModel)
def get_single_blog(blogId:int,db:Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == blogId).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    return blog
# we use here "HTTPException" because we want to return 404 status code




@router.delete('/delete/{blogId}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blogId:int,db:Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
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





@router.put('/update/{blogId}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(blogId:int,req:schemas.Blog,db:Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id==blogId)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    else:
        db.query(models.Blog).filter(models.Blog.id==blogId).update({
            models.Blog.title:req.title,
            models.Blog.content:req.content
        },synchronize_session=False)
        db.commit()
        return {"message":"Blog updated successfully"}
    
