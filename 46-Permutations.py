class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def help(trace,cands):
            if not cands: res.append(trace[:])

            for i,c in enumerate(cands):
                trace.append(c)
                help(trace,cands[:i]+cands[i+1:])
                trace.pop()
        help([],nums)
        return res