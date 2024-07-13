# import package
import random

RandomNumber = random.randint(1, 100)

if RandomNumber < 20:
    print("You are really failed", RandomNumber)
else:
    if RandomNumber < 40:
        print("You are failed", RandomNumber)
    elif RandomNumber < 60:
        print("You're good but you have to be repaired", RandomNumber)
    elif RandomNumber < 80:
        print("You're great keep your value", RandomNumber)
    else:
        print("Great! You're awesome!", RandomNumber)

# If-else operation with logical operators

if (RandomNumber > 0) and (RandomNumber < 20):
    print("LO: You are really failed", RandomNumber)
else:
    if (RandomNumber >= 21) and (RandomNumber < 40):
        print("LO: You are failed", RandomNumber)
    elif (RandomNumber >= 40) and (RandomNumber < 80):
        print("LO: You're great keep your value", RandomNumber)
    else:
        print("LO: Great! You're awesome!", RandomNumber)

# if-else online and ternary
# online
if RandomNumber < 50: print("Failed: One line")
# Ternary
print("Pass the exam") if RandomNumber > 50 else print("Fail the exam")
