class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        can_len = len(candidates)
        def help (start, trace, curr_sum):
            if curr_sum == target:
                res.append(trace[:])
                return
            # if curr_sum > target:
            #     return

            for i in range (start, can_len):
                if candidates[i]+curr_sum <= target:
                    # trace.append(candidates[i])
                    help(i,trace+[candidates[i]],candidates[i]+curr_sum)
        help(0,[],0)
        return res 