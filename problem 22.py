# Given a string of length three representing 
# a set (i.e., surrounded by curly braces) such
#  as "{ABC}", write a function that takes the
#  string as an argument and returns a string of 
#  its permutations in comma separated form, such 
#  as "{ABC, ACB, BAC, BCA, CAB, CBA}". Hint:
#      Use multiple for loops.

import itertools
 
if __name__ == '__main__':
 
    nums = list("ABC")
    
    permutations = itertools.permutations(nums)
 
    print({''.join(permutation) for permutation in permutations})

