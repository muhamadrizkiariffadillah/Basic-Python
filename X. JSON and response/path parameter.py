import fastapi
import typing
import pydantic

app = fastapi.FastAPI()


class Users(pydantic.BaseModel):
    id: int
    full_name: str
    username: str
    email: str


def repository_user(user_id: int = None) -> typing.Optional[dict]:
    users = [
        {
            "id": 1,
            "full_name": "Muhamad Rizki",
            "username": "muriarfad",
            "email": "muriarfad@gmail.com",
        },
        {
            "id": 2,
            "full_name": "Kibo",
            "username": "mrafkibo",
            "email": "mrafkibo@gmail.com",
        },
        {
            "id": 3,
            "full_name": "Bokir",
            "username": "bokir",
            "email": "bokir@gmail.com",

        },
    ]
    if user_id is not None:
        for user in users:
            if user["id"] == user_id:
                return user

    return None


def get_user_by_id(user_id: int = None) -> Users:
    """A service for searching user by ID"""
    input_user = repository_user(user_id)
    if input_user is None:
        return Users()

    user = Users(**input_user)
    return user


@app.get("/users/{user_id}", response_model=Users)
def handler_get_user_by_id(user_id: int = None):
    user_info = get_user_by_id(user_id)
    return user_info
