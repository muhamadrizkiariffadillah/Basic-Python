from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class User(BaseModel):
    # Give some information about schema
    username: str = Field(
        alias="name",
        title="The username",
        description="This is the username of user",
        min_length=4,
        max_length=30,
        default="user"
    )

    liked_post: list[int] = Field(
        title="The number of liked posts",
    )


class ProfileInfo(User):
    short_bio: str
    long_bio: str


def get_user_info() -> ProfileInfo:
    profile_info: dict = {
        "short_bio": "This is my bio",
        "long_bio": "This is my long bio",
    }
    user_content: dict = {
        "name": "kibo",
        "profile_info": profile_info,
    }
    users = User(**user_content)
    full_user: dict = {
        **profile_info,
        **users,
    }
    profile = ProfileInfo(**full_user)
    return profile


@app.get("/user/", response_model=ProfileInfo)
def get_user():
    user = get_user_info()

    return user
