from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class ProfileInfo(BaseModel):
    short_bio: str
    long_bio: str


class User(BaseModel):
    username: str
    profile_info: ProfileInfo
    liked_post: list[int] = None


# def get_user_info() -> (str,str):
#     username:str = "Muhamad Rizki"
#     short_description: str = "This is my bio"
#     liked_post:list = None
#     return username,short_description,liked_post

def get_user_info() -> User:
    profile_info: dict = {
        "short_bio": "This is my bio",
        "long_bio": "This is my long bio",
    }
    profile = ProfileInfo(**profile_info)
    user_content: dict = {
        "username": "Muhamad Rizki",
        "profile_info": profile,
    }
    return User(**user_content)


@app.get("/user/", response_model=User)
def get_user():
    user = get_user_info()

    return user
