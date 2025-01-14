class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def help(val, trace, start):
            if val == 0:
                res.append(trace[:])
                return
            if val < 0:
                return
            
            for i in range(start,n):
                if candidates[i] <= val:
                    trace.append(candidates[i])
                    help(val-candidates[i], trace, i)
                    trace.pop()
        help(target,[],0)
        return res