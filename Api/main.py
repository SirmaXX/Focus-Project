from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def api_index():
    return {"Hello": "Worlsd"}