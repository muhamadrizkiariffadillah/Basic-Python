import random

Counter = random.randint(1, 10)
for x in range(Counter):
    print(x, end=" ")

# Iteration in list
MyList = [x for x in range(random.randint(20, 25), random.randint(25, 31))]
print("\nIteration in list")
for x in MyList:
    print(x, end=",")

# Nested loop
print()
# Input = int(input("\nEnter a number of star: "))
Input = random.randint(0, 5)
for x in range(Input):
    for y in range(0, x + 1):
        print("*", end=" ")
    print()

# Looping using while
x: int = 0
while x < Counter:
    print(x, end=" ")
    x += 1

# break and continue:
# unlimited looping
Count: int = 0
UnlimitedLoop: bool = True
while UnlimitedLoop:
    Count += 1
    if Count == 100:
        UnlimitedLoop = False
    elif Count % 2 == 1:
        continue
    elif Count % 2 == 0:
        print(Count)
