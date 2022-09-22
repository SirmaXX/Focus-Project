

from fastapi import FastAPI
from routers.users import usersroute
from routers.jobs import jobsroute


app = FastAPI()
app.include_router(usersroute, prefix="/users")
app.include_router(jobsroute, prefix="/jobs")

@app.get("/")
async def api_index():
    return {"Hello": "Worlsd"}