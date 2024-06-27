# parent class

class Person:
    def __init__(self, fname: str, lname: str):
        self.fname = fname,
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"


# child class
class Student(Person):
    # super function that will make child class inherit all methods and properties from its parent
    def __init__(self, fname, lname, score):
        super().__init__(fname, lname)
        self.score = score


# variable
student = Student("Muhamad Rizki", "Arif Fadillah", 90)
print(student,student.score)