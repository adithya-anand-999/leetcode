class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def help(sum,trace,start):
            if sum == 0: 
                res.append(trace[:])
                return
            if sum < 0: return

            for i in range(start,n):
                trace.append(candidates[i])
                help(sum-candidates[i], trace, i)
                trace.pop()
        help(target,[],0)
        return res