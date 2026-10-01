# Two instances of recursion
# 1. Recursion is used as a technique in which a function makes one or more calls to itself (main instance)
# 2. When a data structure uses smaller instances of the exact same type of data structure when it represents itself

def factorial(n: int) -> int:

    if n <= 1: # base case/exit condition
        return 1
    else:
        return n * factorial(n - 1) # recursive
    
print(factorial(5))