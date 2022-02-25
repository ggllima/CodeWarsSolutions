# Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
# without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(string):
    list_of_strings = []
    if len(string):
        if string[:] != string[0] * len(string):
            for word in range(len(string)):
                if string[word-1] != string[word] or len(string) == 1:
                    list_of_strings.append(string[word])
        else:
            list_of_strings.append(string[0])
    return list_of_strings