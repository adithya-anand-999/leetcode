class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def help(val, trace, start):
            # print(trace)
            if val == 0:
                # The issue might be that the same trace is being modified, they all point to the same trace list. 
                res.append(trace[:])
                return
            if val < 0:
                return 
            
            for i in range(start, n):
                c = candidates[i]
                if c <= val:
                    trace.append(c)
                    help(val-c, trace, i)
                    trace.pop()

        help(target, [], 0)
        return res