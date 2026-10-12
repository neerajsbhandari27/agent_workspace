from pydantic import BaseModel, EmailStr
from typing import Dict, List

class UserModel(BaseModel):
    name:str
    email:EmailStr
    password:str