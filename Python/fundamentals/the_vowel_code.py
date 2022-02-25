# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

# For example, decode("h3 th2r2") would return "hi there".

# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.


def encode(string):
    vowel_dict = {'a':'1','e':'2','i':'3','o':'4','u':'5'}
    for word in string:
        if word in vowel_dict.keys():
            string = string.replace(word,vowel_dict[word])
    return string

def decode(string):
    vowel_dict = {'a':'1','e':'2','i':'3','o':'4','u':'5'}
    for word in string:
        if word in vowel_dict.values():
            index = list(vowel_dict.values()).index(word)
            vowel = list(vowel_dict.items())[index][0]
            string = string.replace(word,vowel)
    return string