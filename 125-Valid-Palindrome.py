class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        
        l,r = 0, len(s)-1
        while l<r:
            if s[l] not in chars:
                l+=1
                continue
            if s[r] not in chars:
                r-=1
                continue
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
        