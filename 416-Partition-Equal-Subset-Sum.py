class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum%2 != 0: return False

        tar = total_sum//2
        dp = [False] * (tar+1)
        dp[0] = True

        for n in nums:
            for j in range(tar,n-1,-1):
                dp[j] = dp[j] or dp[j-n]
        return dp[tar]