from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas
from .. import schemas , models
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash


router = APIRouter(
    prefix="/user",
    tags=["User Routes"]
)



@router.post('/create',status_code=status.HTTP_201_CREATED)
def create_user(req:schemas.User,db:Session = Depends(get_db)):
    hashPassword = Hash.bcrypt(req.password)
    new_user = models.User( name=req.name, email=req.email, password=hashPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"User created successfully"}




@router.post('/login',status_code=status.HTTP_200_OK)
def login_user(req:schemas.Login,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Crendentails")
    if not Hash.verify(req.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Crendentails")
    return {"message":"User logged in successfully"}



@router.get('/{userId}',status_code=status.HTTP_200_OK,response_model=schemas.ResponseModelUser)
def get_single_blog(userId:int,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == userId).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    return user
# we use here "HTTPException" because we want to return 404 status code