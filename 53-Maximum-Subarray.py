class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #you have to select the max subarray in nums, not selecting anything is not valid. If it was they would have told us in the specs. 
        maxSum = curSum =  nums[0]

        for i in range(1, len(nums)):
            if curSum < 0:
                curSum = nums[i]
            else:
                curSum += nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum
        