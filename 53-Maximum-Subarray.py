class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = temp_sum = nums[0]

        for r in nums[1:]:
            if temp_sum < 0:
                temp_sum = 0
            temp_sum += r
            max_sum = max(max_sum,temp_sum)
        return max_sum