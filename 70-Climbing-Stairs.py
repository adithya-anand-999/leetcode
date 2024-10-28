class Solution:
    def climbStairs(self, n: int) -> int:
        # count = 0
        # def help(n):
        #     nonlocal count
        #     if n < 0: return
        #     if n == 0: count+=1
        #     help(n-1)
        #     help(n-2)
        # help(n)
        # return 
        
        if n == 1:return 1

        stepP1 = 1
        stepP2 = 2
        res = 2
        for i in range(2,n):
            res = stepP1 + stepP2
            stepP1, stepP2 = stepP2, res
        return res
