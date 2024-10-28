class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        res = 0
        addedOne = False

        for c in s:
            if c not in freq:
                freq[c] = [1,True]
            else:
                freq[c][0] += 1
                freq[c][1] = not freq[c][1]
        for cnt,odd in freq.values():
            if odd:
                res+=cnt-1
                addedOne = True
            else:
                res+=cnt
        if addedOne:res+=1
        return res
