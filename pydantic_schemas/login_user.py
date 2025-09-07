from pydantic import BaseModel



class UserLogin(BaseModel):
    name: str
    email: str
    password: str