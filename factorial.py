# Factorial
# To check an object type we use isinstance. It takes two parameter one object, 
# two data type to check.
# We can also use is_digit

# Factorial is the sum of all numbers from 1 to n.
# Get and print an object’s type: type()
'''
Get and print an object’s type: type()
Get and print an object’s type: isinstance()
Get and print an object’s type: __class__ attribute
In Python, everything is an object, and each object has characteristics of its own. 
The ‘__class__’ attribute is the only one that can return the class type of the object. 
The __class__ attribute in Python can also be used to verify object type in addition to built-in functions.

Each Python object has an attribute called __class__ that contains the object’s class information. 


'''


def factorial(n):
	fact = 1
	input_n = input()
	if isinstance(n, int)::
		return fact*i for i in range(input_n)
	elif isinstance(n, str):
		return fact*i for i in range(int(2, input_n+1))


# 1. Using Iteration (For Loop)
# This is a straightforward approach where we multiply numbers in a loop.

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 2. Using Recursion
# A recursive function calls itself to compute the factorial.

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# 3. Using Python's math.factorial() Function
# Python provides a built-in method in the math library for calculating factorials.


import math

def factorial_builtin(n):
    return math.factorial(n)


# 4. Using reduce() from functools
# This approach uses functional programming with reduce() to calculate the factorial.


from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


# 5. Using List Comprehension
# This approach multiplies elements in a list comprehension.

def factorial_list_comprehension(n):
    result = 1
    [result := result * i for i in range(2, n + 1)]
    return result


# 6. Using a While Loop
# An iterative approach, but using a while loop.

def factorial_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

    
# 7. Using Memoization (Caching)
# For large inputs, recursion may be inefficient. Memoization stores previously calculated results for reuse.

factorial_cache = {}

def factorial_memoization(n):
    if n in factorial_cache:
        return factorial_cache[n]
    if n == 0 or n == 1:
        factorial_cache[n] = 1
    else:
        factorial_cache[n] = n * factorial_memoization(n - 1)
    return factorial_cache[n]