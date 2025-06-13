""" 
Consider an array of non-negative integers. A second array is formed by shuffling the elements
of the first array and deleting a random element. Given these two arrays, find which element is
missing in the second array. 
"""
import collections

def finder(arr1: list, arr2: list) -> int:
    
    num_of_num = {}

    # Puts all elements of arr2 as key with value of counts they occur
    for i in range(len(arr2)):
        if arr2[i] not in num_of_num:
            num_of_num.update({str(arr2[i]): 1})
        else:
            num_of_num[str(arr2[i])] += 1

    # Compares with arr1
    for i in range(len(arr1)):
        # Returns if missing number is not seen in arr2
        if str(arr1[i]) not in num_of_num:
            return arr1[i]
        else:
            num_of_num[str(arr1[i])] -= 1

    # Checks for duplicates. All unique value counts should be 0
    for key, val in num_of_num.items():
        if val != 0:
            return key

    return

print(finder([5, 5, 7, 7], [5, 7, 7]))
print(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
print(finder([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]))

def finder2(arr1: list, arr2: list) -> int:

    # default dictionary takes integer keys to avoid key errors if key cannot be found in dictionary
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1 # Allowed to do this with default dict even if the key doesn't exist yet in default dict

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

print(finder2([5, 5, 7, 7], [5, 7, 7]))
print(finder2([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
print(finder2([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]))

def finder3(arr1: list, arr2: list) -> int:

    result = 0

    for num in arr1 + arr2:
        result ^= num # Performs and XOR between numbers (result and num) in arr1 + arr2
        # If they are different, it stores abs difference (since they are bitwise comparisons, they aren't negative) in result
        # If they are the same, sets result to 0 
        #print(result)

    return result

print(finder3([5, 5, 7, 7], [5, 7, 7]))
print(finder3([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
print(finder3([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]))