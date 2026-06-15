from fastapi import FastAPI
from database.database import Base, engine
from contextlib import asynccontextmanager


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Application Start!")
    Base.metadata.create_all(engine)
    yield
    print("Application Stop!")

app = FastAPI(lifespan=life_span)
