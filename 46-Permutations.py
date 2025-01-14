class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def help(trace,candidates):
            if candidates == []:
                res.append(trace[:])
                return
            
            # print(candidates)
            for i in range(len(candidates)):
                trace.append(candidates[i])
                help(trace,candidates[:i] + candidates[i+1:])
                trace.pop()
        help([],nums)
        return res