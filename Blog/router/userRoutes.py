from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas
from .. import schemas , models
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash


router = APIRouter()



@router.post('/create-user',status_code=status.HTTP_201_CREATED,tags=['User'])
def create_user(req:schemas.User,db:Session = Depends(get_db)):
    hashPassword = Hash.bcrypt(req.password)
    new_user = models.User( name=req.name, email=req.email, password=hashPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"User created successfully"}




@router.get('/user/{userId}',status_code=status.HTTP_200_OK,tags=['User'],response_model=schemas.ResponseModelUser)
def get_single_blog(userId:int,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == userId).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    return user
# we use here "HTTPException" because we want to return 404 status code