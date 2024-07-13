from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    profile_info: str

@app.post("/users",)