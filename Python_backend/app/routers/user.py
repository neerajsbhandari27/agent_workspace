from fastapi import APIRouter, Request,status
from app.schemas.users import UserModel
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

router=APIRouter(tags=["User"])



@router.post("/users",
response_model=UserModel,
status_code=status.HTTP_201_CREATED,
response_model_by_alias=False)

async def create_user(user:UserModel,request:Request):
    """
    insert a user in record"""
    db=request.app.database
    new_user = user.model_dump(by_alias=True, exclude=["id"])
    result=await db["users"].insert_one(new_user)
    new_user["_id"]=result.inserted_id
    return new_user


@router.get("/users")
async def get_user(request:Request):
    db=request.app.database
    users=await db["users"].find().to_list(length=100)
    return jsonable_encoder(users,
    custom_encoder={ObjectId:str})