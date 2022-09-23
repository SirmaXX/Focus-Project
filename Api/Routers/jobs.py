from fastapi import APIRouter


jobsroute = APIRouter()


jobsroute.get('/info')
def books():
    return {"detail": "This book info is from the book APIRouter",
    "name": "Hello",
    "ISBN": "32DS3"}
