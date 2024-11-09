class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        curWin = set()
        l = 0

        for r in range(len(s)):
            while s[r] in curWin:
                curWin.remove(s[l])
                l+=1
            curWin.add(s[r])
            res = max(res, len(curWin))
        return res