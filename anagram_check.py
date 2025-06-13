def anagram(s1: str, s2: str) -> bool:
    """Checks if two strings are anagrams of each other"""
    
    # Removes spaces and sets all to lower case
    s1.replace(' ','').lower()
    s2.replace(' ','').lower()

    # Returns false if string lengths aren't the same
    if len(s1) != len(s2):
        return False
    
    num_of_letters = {}

    # Gets occurrences of all letters inside of s1
    for i in range(len(s1)):
        if s1[i] not in num_of_letters:
            num_of_letters.update({s1[i]: 1})
        else:
            num_of_letters[s1[i]] += 1

    # Compares s2 with s1
    for i in range(len(s2)):
        # Returns false if there is a letter in s2 that isn't in s1
        if s2[i] not in num_of_letters:
            return False
        else:
            num_of_letters[s2[i]] -= 1

    # Returns false if not all letters have equal number of occurrences in s1 and s2
    for val in num_of_letters.values():
        if val != 0:
            print(num_of_letters)
            return False

    return True

print(anagram('dgoss', 'ddogs'))
print(anagram('goad', 'dogs'))
print(anagram('aa', 'bb'))
print(anagram('yes', 'sye'))