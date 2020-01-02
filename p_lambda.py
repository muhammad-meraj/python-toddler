# Lambda
def my_def(n):
    return lambda x: x * n

doubler = my_def(2)
tripler = my_def(3)

print doubler(2)
print tripler(2)

# Map
# Applies method to each element of list/iterable
f = lambda x: x*2
l = map(f, [1,2,3,4,5])
print l

# Filter
"""
The filter() function is used to create an output list consisting of 
values for which the function returns true. The syntax of it is as follows:

SYNTAX:

filter(function, iterables)

function can lambda or user-defined function
"""

def big_numbers_filter(x):
    if x > 1000:
        return True
    else: 
        return False

l = filter(big_numbers_filter, [100, 3, 2000, 3000, 4000, 4])
print l


# above filter with lambda
l = filter(lambda x: x>1000, [100, 3, 2000, 3000, 4000, 4])
print l

# Reduce
# Reduce function applies a function on iterables to reduce it to one value
from functools import reduce
# sum of all elements in list
l = reduce(lambda a,b: a+b, [1,2,3,4,5])
print l