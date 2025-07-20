class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def help(tot, trace, start):
            if tot == target: 
                res.append(trace[:])
                return
            if tot > target: return
            for i,c in enumerate(candidates[start:]):
                if c <= target-tot:
                    trace.append(c)
                    help(tot+c, trace, start+i)
                    trace.pop()
        help(0,[],0)
        return res