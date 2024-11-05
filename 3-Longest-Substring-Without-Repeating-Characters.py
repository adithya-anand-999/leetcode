class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        wind = set()
        res = 0


        for r in s:
            while r in wind:
                wind.remove(s[l])
                l+=1
            wind.add(r)
            res = max(res, len(wind))
        return res