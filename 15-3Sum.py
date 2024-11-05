class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,n-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l+1<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r-1 and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    r-=1
        return res


