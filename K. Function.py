# Chapter 1
import datetime
import math

import bcrypt


def say_hello():
    # Comment to explain the function
    """This function says hello to the user"""

    print("Hello World")


say_hello()


def print_something():
    print("Hello")
    today = datetime.datetime.today()
    print(today)
    for x in range(1, 6):
        print(x, end=" ")


print()
print_something()


# Chapter 2: Parameter Function and Argument.

def calculate_circle_area(r):
    pi: float = math.pi
    area = pi * (r ** 2)
    print(area)


print()
calculate_circle_area(388)


def calculate_circle_areas(message: str, r: int):
    pi: float = math.pi
    area = pi * (r ** 2)
    print(f"{message} {area}")


calculate_circle_areas("The number of area is", 500)


# Chapter 3: Return Value

def calculate_cube_area(s: int):
    return s ** 3


def calculate_cube_circumference(s: int):
    return 6 * (s * 4)


cube = calculate_cube_area(10)
print(cube)
cube = calculate_cube_circumference(25)
print(cube)


# Chapter 4: Data types of return value


def calculate_circle_area_1(r: int) -> float:
    return math.pi * (r ** 2)


circle_1 = calculate_circle_area_1(50)
print(circle_1)


def login(username: str, password: str) -> dict:
    user_password = password.encode("utf-8")
    user: dict = {
        "Username": username,
        "Password": bcrypt.hashpw(user_password, bcrypt.gensalt())
    }
    return user


UserLogin: dict = login("Muhamad Rizki Arif Fadillah", "buahahahaha")
print(UserLogin)


# Chapter 5: Keyword pass

# Need to complete later

def transpose_matrix(matrix):
    pass


def user_login(username: str, password: str) -> (dict, NameError):
    user: dict = {
        "Username": username,
        "Password": bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    }
    return user, None


print(user_login("kibo", "password"))
