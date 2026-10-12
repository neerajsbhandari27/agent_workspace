import asyncio
import os
from dotenv import load_dotenv
import logging
from fastapi import FastAPI
from pymongo import AsyncMongoClient
from contextlib import asynccontextmanager


logger=logging.getLogger("simplelogger")
logger.setLevel(logging.DEBUG)
load_dotenv()


@asynccontextmanager
async def db_lifespan(app:FastAPI):
    try:
        app.mongodb_client=AsyncMongoClient(
            os.getenv("DATABASE_URL")
        )
        app.database=app.mongodb_client.get_database("agent_workspace")
        await app.database.command("ping")
        logger.info("Mongo db connected")
        yield
    finally:
        await app.mongodb_client.close()
        logger.info("mongo db closed")


app = FastAPI(lifespan=db_lifespan)