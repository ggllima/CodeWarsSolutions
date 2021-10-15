# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

# Note: anagrams are case insensitive

# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

# Examples
# "foefet" is an anagram of "toffee"

# "Buckethead" is an anagram of "DeathCubeK"

def is_anagram(test, original):
    test = test.lower()
    test = list(test)
    test.sort()
    original = original.lower()
    original = list(original)
    original.sort()
    if test == original:
        return True
    return False