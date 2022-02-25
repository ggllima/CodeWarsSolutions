# Create a function named divisors/Divisors that takes an integer n > 1 
# and returns an array with all of the integer's divisors(except for 1 and the number itself), 
# from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) 
# (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

# Example:
# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"


# first solution (a little slow):

def divisors(n):
    # list of integers from 2 to selected integer
    list_integers = list(range(2,n+1))
    # empty list to get possible dividers
    divisors = []
    for element in list_integers:
        for comparison_element in list_integers:
            if comparison_element%element == 0 and comparison_element!= element:
                list_integers.remove(comparison_element)
            comparison_element+=1
    if n in list_integers:
        return "{} is prime".format(n)
    else:
        for index in range(2,n):
            if n%index == 0:
                divisors.append(index)
        return divisors
    
# second solution (faster):

def divisors(integer):
    list_of_integers = [number for number in range(2,integer) if integer%number == 0]
            
    if len(list_of_integers) == 0: return str(integer) + " is prime"
    return list_of_integers