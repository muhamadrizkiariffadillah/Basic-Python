# Lambda is a small anonymous function
from typing import Callable, Any

first: Callable[[Any], int | Any] = lambda x: 100 if x <= 0 else x + x
print(first(0))

# Multiply arguments

multi = lambda x, y: x * y
print(multi(10, 29))
