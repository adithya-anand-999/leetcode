class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(l,r):
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                r+=1
            return (l+1,r-1)
        
        l,r = 0,0
        for i in range(n):
            oL,oR = expand(i,i)
            eL,eR = expand(i,i+1)

            if eR-eL>r-l: l,r = eL,eR
            if oR-oL>r-l: l,r = oL,oR
        return s[l:r+1]