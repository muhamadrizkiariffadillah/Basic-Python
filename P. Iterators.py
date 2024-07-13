# Lists, tuples and sets are all iterable objects.
myList: list = [1, "Muhamad Rizki", 125.5, None]
Iterable = iter(myList)

print(next(Iterable))
print(next(Iterable))
print(next(Iterable))
print(next(Iterable))


# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))

# Stop iteration
class Numbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
Num = Numbers()
Iter = iter(Num)

for x in Iter:
    print(x,end=" ")
