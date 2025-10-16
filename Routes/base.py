from fastapi import FastAPI , APIRouter

base_router = APIRouter()

@base_router.get("/")
def welcome_back():
    return {
        "message" : "hello yy" }
