import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # you have to go n-1 right and m-1 down in every valid path. 
        # the number of combinations with that. 
        # right = r and down = d
        # every path has r*(n-1) and d*(m-1). How many combinations can I make with that, where order matters. 

        # the number of permuations with  r*(n-1) and d*(m-1). I dont even need to know what they are, just how many exist. There is a math formula for this. 
        # actually this is wrong, as the r or d you choose does not matter. All r's and d's are identical. THere is no I choose the 2nd r vs 1st r. 
        # we need unique permutations which is this. factorial of population/factorial of frequenc of all elements that make up the population. 
        d,r = m-1,n-1
        return (math.factorial(d+r))//(math.factorial(d) * math.factorial(r))