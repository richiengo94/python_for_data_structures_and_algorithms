# Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer

def rec_sum(n: int) -> int:

    if n == 0:
        return 0
    else:
        return n + rec_sum(n - 1)
    
print(rec_sum(4))

# Given an integer, create a function which returns the sum of all the individiual digits in that integer

def sum_func(n: int) -> int:

    if(len(str(n)) == 1):
        return n
    else:
        return (n % 10) + sum_func(int(n / 10))
    
print(sum_func(281))

# Create a function called word_split() which takes in a string phrase and a set of list_of_words.
# The function will then determine if it is possible to split the string in a way in which words can
# be made from the list of words. You can assume the phrase will only contain words found in the 
# dictionary if it is completely splittable.

def word_split(phrase: str, list_of_words: list[str], output = None):

    if not output:
        output = []

    for word in list_of_words:
        if phrase.find(word) == 0:

            output.append(word)

            return word_split(phrase[len(word):], list_of_words, output)
    
    return output
        
print(word_split("themanran", ["the", "man", "ran"]))
print(word_split("ilovedogsJohn", ["i", "am", "a", "dogs", "lover", "love", "John"]))
print(word_split("themanran", ["clown", "ran", "man"]))