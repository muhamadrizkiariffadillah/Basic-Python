# string for text
FullName: str = "Muhamad Rizki Arif Fadillah"
Introduction: str = """
My full name is Muhamad Rizki Arif Fadillah, but my friends address me kibo.
My passion is programming, data science and hacking.
So I am proud of my self.
'Keep learning to invest my self in technology and creativity industry' 
"""

# int for integer without decimal
MyAge: int = 25

# float for decimal
MyTall: float = 170.1

# complex
Complex: complex = 120j

# bool for boolean
Handsome: bool = True
Ugly: bool = False

# List for array and mutable
MyList: list = ["Muhamad Rizki", 170, 169.9, True]

# Tuple for array and immutable
MyTuple: tuple = (1, 1, "Muhamad")

# Set for array can't be duplicated and using index but can access using looping
MySet: set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Dictionary for key and value
MyDictionary: dict = {
    "FullName": "Muhamad Rizki Arif Fadillah",
    "Age": 25,
    "Tall": 169.9,
    "Handsome": True,
}

print(FullName, Introduction, MyAge, MyTall, Complex, Handsome, Ugly, MyList, MyTuple, MySet, MyDictionary)
