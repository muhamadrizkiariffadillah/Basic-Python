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


# *args = for many arguments
def iteration(*args):
    for x in args:
        print(f"{x}", end=" ")
    print()


iteration([x for x in range(1, 5)])


# kwargs = Keyword arguments.
def kewyargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} == {value}")


kewyargs(first_name="Muhamad Rizki", last_name="Arif Fadillah", age=25, handsome=True, whatever=None)


# default parameter
def full_name(fullname: str = "Username", last_name: str = "Arif Fadillah"):
    return fullname + " " + last_name


print(full_name())
print(full_name("Kibo", "Bokir"))

# Typing
from typing import Union
from typing import Optional


def return_value(a, b: int) -> Union[float, None]:
    c = float()
    if a and b != 0:
        c = a / b
        return c
    else:
        return None


print(return_value(50, 3))
print(return_value(100, 0))


def division(a, b: int) -> Optional[float]:
    if a and b != 0:
        return a / b
    else:
        return


print(division(10, 3))
print(division(1, 0))


def test_unpack(input_list: list[str], index: int) -> str:
    return input_list[index]


print(test_unpack("Muhamad", 0))
