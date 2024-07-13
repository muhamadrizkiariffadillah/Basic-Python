MyList: list = [x for x in range(10) if x % 2 == 0]
print(MyList, type(MyList), len(MyList))

ExampleList: list = [1, 3.3, 'Kibo', True, None]
print(ExampleList, type(ExampleList), len(ExampleList))

# Add to list
EmptyList: list = []
for x in range(1, 10):
    if x % 2 == 1:
        EmptyList.append(x)
print(EmptyList)

# Indexing
print(ExampleList[1])
print(ExampleList[2])
# Iteration
for x in range(len(ExampleList)):
    print(ExampleList[x], end=" ")

# Slicing
print(ExampleList[:2])
print(ExampleList[2:5])
print(ExampleList[-3:-1])
# Reverse the list
print(ExampleList[::-1])
# Concat list
ConcatList = MyList + ExampleList
print(ConcatList)
# Pop
ConcatList.pop(2)
print(ConcatList)

# Nested list
VectorList: list = [[MyList], [ExampleList]]
print(VectorList)

# Insert List
# MyList.insert(#index,#value)
MyList.insert(3, 30)
print(MyList)

# Delete an element
print(MyList.pop(3))

del MyList[0:2]
print(MyList)

# Searching the index number in element
print(MyList.index(8))

# List comprehension
seq = [x * 2 for x in range(5)]
print(seq)
seq = [x for x in range(10) if x % 2 == 1]
print(seq)
seq = [x * (2 if x % 2 == 0 else 3) for x in range(10)]
print(seq)
seq = [x + y for x in MyList for y in MyList]
print(seq)
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
seq = [[row[x] for row in matrix] for x in range(4)]
print(seq)
