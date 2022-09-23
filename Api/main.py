from flask_sqlalchemy import SQLAlchemy
from fastapi import FastAPI
from Routers.users import usersroute
from Routers.jobs import jobsroute

import os
import json


app = FastAPI()

app.include_router(usersroute, prefix="/users")
app.include_router(jobsroute, prefix="/jobs")



@app.get("/")
async def api_index():
    return {"Hello": "Worlsd"}