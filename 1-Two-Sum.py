class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortNums = sorted(nums)

        l,r = 0, len(sortNums)-1
        while l<r:
            sum = sortNums[l] + sortNums[r]
            if sum == target:
                return [nums.index(sortNums[l]), len(sortNums) - 1 - nums[::-1].index(sortNums[r])]
            if sum > target:
                r-=1
            else:
                l+=1