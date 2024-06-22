# Chapter 1
FirstTuple: tuple = (1, 2.2, "Kibo", True, None)

print(FirstTuple, type(FirstTuple), len(FirstTuple))

# Chapter 2 Access element of tuple
print(FirstTuple[1])
print(FirstTuple[2])

# Capter 3 Loopin in tuple
for x in FirstTuple:
    print(x, end=" ")
print()

for x, y in enumerate(FirstTuple):
    print(f"Index : {x}, Value : {y}")
# Chapter 4 Nested Tuple
NestedTuple: tuple = (
    (1, 2, 3),
    (4, 5, 6),
)
for row in NestedTuple:
    for cel in row:
        print(cel, end=",")
    print()

# Chapter 5 Check if the value is available or not
n = 6
for cel in NestedTuple:
    if n in cel:
        print(f"6 is available")
    else:
        print("The number isn't available")

# Chapter 6 List and Tuple.
data = [
    (1,2,3, [4,5,6]),
    (7,8,9,[10,11,12]),
]

data.append((13,14,16,[17,18,19]))

for row in data:
    for cel in row:
        print(cel,end=" ")

