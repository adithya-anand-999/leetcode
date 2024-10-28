class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        res = 0
        seenOne = False

        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c]+=1
        
        for cnt in freq.values():
            if cnt%2 == 0:
                res+=cnt
            else:
                seenOne = True
                res+=cnt-1
        if seenOne: res+=1
        return res