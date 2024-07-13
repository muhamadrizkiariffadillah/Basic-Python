# Chapter 1
FirstSet: set = {1, 'abc', False, None, ('Pizza', 'Spagethi')}
print(FirstSet)
print(len(FirstSet))

# Chapter 2
for x in FirstSet:
    print(x, end=" ")
print()

# Set automatic deletes duplicate value.
MySetNumber: set = {1, 2, 3, 3, 2, 1, 4, 5, 6, 7, 8, 9, 6, 3, 4, 5, 6}
print(MySetNumber)

# Casting list to set, as default remove duplicate value
MyListNumber: list = [1, 2, 3, 3, 2, 1, 4, 5, 6, 7, 8, 9, 6, 3, 4, 5, 6]
print(MyListNumber)
MyUniqueSet: set = set(MyListNumber)
print(MyUniqueSet)
MyListNumber = list(MyUniqueSet)
print(MyListNumber)
# Check membership in set
MemberSet: set = {"Muhamad", "Rizki", "Arif", "Fadillah"}
toCheck = "Fadillah"

if toCheck in MemberSet:
    print(f"{toCheck} is available in set")

# Chapter 3
# Add elements in set
EmptySet: set = set()
for x in range(1, 6):
    EmptySet.add(x)
print(EmptySet)

# Add elements using set comprehension
ComSet: set = {x for x in range(1, 6)}
print(ComSet)

# Delete random elements in set
MembershipSet: set = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
print(MembershipSet)
print(MembershipSet.pop())
print(MembershipSet.pop())

# Delete Specific
MembershipSet: set = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
print(MembershipSet)
MembershipSet.discard('aragorn')
print(MembershipSet)
MembershipSet.discard('gimli')
print(MembershipSet)
MembershipSet.discard('legolas')
print(MembershipSet)

# Clear set
MembershipSet: set = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
print(MembershipSet)
MembershipSet.clear()
print(MembershipSet)

# Check intersection between sets
MembershipSet: set = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
Hobbits: set = {'aragorn', 'sam', 'merry', 'kibo'}
Duplicate = MembershipSet.intersection(Hobbits)
print(Duplicate)

# Check membership subset
CheckSubSet: set = {'pippin', 'sam', 'merry'}
res = CheckSubSet.issubset(MembershipSet)
print(res)

# Checking superset
Res: bool = MembershipSet.issuperset(CheckSubSet)
print(Res)

# Check membership
res_3 = MembershipSet.isdisjoint({'aragorn'})
print(res_3)

# Update value
MembershipSet.update({'Kibo'})
print(MembershipSet)
MembershipSet.update({'Bokir'})
print(MembershipSet)

# Union
UnionSet: set = {"Python Developer","Cyber Security Engineer"}
NewSet: set = MembershipSet.union(UnionSet)
print(NewSet)

# Chapter 4
# Bitwise operation in set
Set_1: set = set('abracadra')
Set_2: set= set('tetap tersenyum')

bw = Set_1 | Set_2
print(bw)
bw = Set_1 & Set_2
print(bw)
bw = Set_1 ^ Set_2
print(bw)

# Chapter 6
# FrozenSet
A = frozenset('abracadabra')
print(A)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()		Sorts the list