class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        l = 0
        n = len(nums)
        for i in range(3):
            for r in range(n):
                if nums[r] == i:
                    nums[l],nums[r] = nums[r],nums[l]
                    l+=1
        return nums