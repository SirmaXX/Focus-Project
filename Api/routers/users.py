from fastapi import APIRouter


usersroute = APIRouter()

@usersroute.get('/info')
def novels():
    return {"detail": "This novel info is from the novel APIRouter",
    "name": "I am good",
    "publication": "Kaustubh"}
