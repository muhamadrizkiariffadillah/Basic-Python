import fastapi
from fastapi import Depends
from pydantic import BaseModel, Field
from typing import Union

app = fastapi.FastAPI()


class User(BaseModel):
    Id: int
    Name: str
    Email: str
    Liked_post: list[int]


users1 = {
    "Id": 1,
    "Name": "Muhamad Rizki",
    "Email": "muriarfad@gmail.com",
    "Liked_post": [500]
}


def get_user_indo(user: dict) -> Union[dict, TypeError]:
    users = user
    return users, None


@app.get("/v1/user/", response_class=fastapi.responses.JSONResponse)
def get_user():
    user = {
        "Id": 1,
        "Name": "Muhamad Rizki",
        "Email": "muriarfad@gmail.com"
    }
    user = get_user_indo(user)
    return user


@app.get("/v2/user", response_model=User)
def get_user_v2():
    users, err = get_user_indo(users1)
    if err is not None:
        return users, err
    return users


@app.get("/user-info", response_model=User)
def get_user_info():
    users, err = get_user_indo(users1)
    return users

