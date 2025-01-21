class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(l,r):
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                r+=1
            return (l+1,r)
        
        start,end = 0,0
        for i in range(n):
            oL,oR = expand(i,i)
            eL,eR = expand(i,i+1)

            if oR-oL > end-start:
                start,end = oL,oR
            if eR-eL > end-start:
                start,end = eL,eR
        return s[start:end]