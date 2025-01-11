class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        valid = 'abcdefghijklmnopqrstuvwxyz0123456789'
        l,r = 0,len(s)-1
        while l<r:
            while (l+1)<=r and s[l] not in valid: l+=1
            while l<=(r-1) and s[r] not in valid: r-=1
            if s[l] != s[r]: return False
            l+=1
            r-=1
        return True