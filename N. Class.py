# Python is an object-oriented programming language.
import datetime

import bcrypt


class MyClass:
    x: int = 5


p = MyClass()
print(p.x)


#  The __init__ function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Kibo", 25)
print(person.name)
print(person.age)


# The __str__ function controls what should be returned when the class object is represented as a string
class Student:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"{self.name} {self.age} {self.email}"


student = Student("Kibo", 24, "muriarfad@gmail.com")
print(student)


# Object method
class Employee:
    def __init__(self, id: int, fullname: str, email: str, password: str, created_at: str, updated_at: str):
        self.id = id
        self.fullName = fullname
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"{self.id} {self.fullName} {self.email} {self.password} {self.created_at} {self.updated_at}"


employee: dict = {
    "id": 1,
    "full_name": "Muhamad Rizki Arif Fadillah",
    "email": "muriarfad@gmail.com",
    "password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "created_at": str(datetime.datetime.now()),
    "updated_at": str(datetime.datetime.now()),
}

first_employee = Employee(
    id=employee['id'],
    fullname=employee['full_name'],
    email=employee['email'],
    password=employee['password'],
    created_at=employee['created_at'],
    updated_at=employee['updated_at']
)

print(first_employee)

