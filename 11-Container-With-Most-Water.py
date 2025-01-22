class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0,n-1
        max_volume = 0

        while l<r:
            l_val,r_val = height[l],height[r]
            if l_val>r_val:
                max_volume = max(max_volume, r_val*(r-l))
                r-=1
            else:
                max_volume = max(max_volume,l_val*(r-l))
                l+=1
        return max_volume