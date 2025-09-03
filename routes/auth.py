import bcrypt
from fastapi import Depends, HTTPException
from database import get_db
from models.user import User
from pydantic_schemas.user_create import UserCreate
from fastapi import APIRouter
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/signup")
def signup_user(user: UserCreate,db:Session=Depends(get_db)):
    user_db=db.query(User).filter(User.email==user.email).first()
    
    if user_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        hashed_password=bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        new_user=User(name=user.name, email=user.email, password=hashed_password)
        db.add(new_user)
        db.commit()
        return user_db

