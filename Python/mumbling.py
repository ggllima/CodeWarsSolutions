# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


# first solution
def accum(x):
    return '-'.join([k.upper() + k.lower() * i for i,k in enumerate(x)])

# second solution
def accum(x):
    l = []
    k = 1
    for i in x:
        l.append(i * k)
        k+=1
    w = [i.capitalize() for i in l]
    w = '-'.join(w)
    return w

