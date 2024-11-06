class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        #you have to sort nums inorder to do binary search
        nums.sort()
        for i in range(n-2):
            l,r = i+1,n-1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    r-=1
        return list(res)