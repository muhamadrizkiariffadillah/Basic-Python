import random

# math operators
FirstNumber: int = random.randint(10, 20)
SecondNumber: int = random.randint(5, 10)

print(FirstNumber, SecondNumber)

# addition
print(FirstNumber + SecondNumber)
# substraction
print(FirstNumber - SecondNumber)
# multiplication
print(FirstNumber * SecondNumber)
# division
print(FirstNumber / SecondNumber)
# modulus
print(FirstNumber % SecondNumber)
# exponent
print(FirstNumber ** SecondNumber)
# floor division
print(FirstNumber // SecondNumber)

# assignment operator
FirstNumber += SecondNumber
# Etc -= /= *= %= //= **=
print(FirstNumber)

# comparison operators
Equal: bool = FirstNumber == SecondNumber
NotEqual: bool = FirstNumber != SecondNumber
MoreThan: bool = FirstNumber > SecondNumber
LessThan: bool = FirstNumber < SecondNumber
EqualOrMoreThan: bool = FirstNumber >= SecondNumber
EqualOrLessThan: bool = FirstNumber <= SecondNumber

print(Equal, NotEqual, MoreThan, LessThan, EqualOrMoreThan, EqualOrLessThan)

# logical operators
And: bool = (FirstNumber > SecondNumber) and (FirstNumber < SecondNumber)
Or: bool = (FirstNumber > SecondNumber) or (FirstNumber < SecondNumber)
Negation: bool = not (FirstNumber > SecondNumber)

print(And, Or, Negation)

print(id(FirstNumber))