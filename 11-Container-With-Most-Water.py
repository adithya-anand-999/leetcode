class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        max_vol = 0

        while l<r:
            hl,hr = height[l],height[r]
            if hl>hr:
                max_vol = max(max_vol, hr*(r-l))
                r-=1
            else:
                max_vol = max(max_vol, hl*(r-l))
                l+=1
        return max_vol
