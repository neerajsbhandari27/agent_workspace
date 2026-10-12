from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt
from datetime import datetime, timedelta
from app.routers.agent import router as agent_router
from app.routers.user import router as user_router
from app.services.database import db_lifespan
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")

app=FastAPI(lifespan=db_lifespan)

def create_token(data:dict):
    
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=45)
    to_encode.update({
        "exp":expire
    })
    token=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token



    
app.include_router(agent_router)
app.include_router(user_router)
@app.get("/health")
def health():
    return {
        "status":"Healthy"
    }

