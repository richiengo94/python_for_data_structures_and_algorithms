# Two instances of recursion
# 1. Recursion is used as a technique in which a function makes one or more calls to itself (main instance)
# 2. When a data structure uses smaller instances of the exact same type of data structure when it represents itself

def factorial(n: int) -> int:

    if n <= 1: # base case/exit condition
        return 1
    else:
        return n * factorial(n - 1) # recursive
    
print(factorial(5))

def sum_list(lst: list[int]) -> int:
    """Grokking Algorithms Exercises 4.1"""
    
    if not lst: # base case 1
        return 0
    elif len(lst) == 1: # base case 2
        return lst[0]
    else: # recursion
        return sum_list(lst[1::]) + lst[0]

print(sum_list([]))
print(sum_list([2]))
print(sum_list([2, 4, 6]))

def n_items_in_list(lst: list[int]) -> int:
    """Grokking Algorithms Exercises 4.2"""

    if not lst: # base case
        return 0
    else: # recursion
        return 1 + n_items_in_list(lst[1::])

print(n_items_in_list([]))
print(n_items_in_list([1]))
print(n_items_in_list([2, 4, 6, 19, 41, 1, 53]))

def max_num_in_list(lst: list[int]) -> int | None:
    """Grokking Algorithms Exercises 4.3"""

    if not lst:
        return None
    else:
        if len(lst) == 2: # base case 1
            return lst[0] if lst[0] >= lst[1] else lst[1]
        elif len(lst) == 1: # base case 2
            return lst[0]
        else: # recursion
            return max_num_in_list(lst[1::])

print(max_num_in_list([]))
print(max_num_in_list([2]))
print(max_num_in_list([1, 4, 3]))