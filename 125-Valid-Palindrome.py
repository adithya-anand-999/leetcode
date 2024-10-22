class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid = 'abcdefghijklmnopqrstuvwxyz1234567890'

        l,r = 0,len(s)-1
        while l<r:
            vl,vr = s[l] in valid, s[r] in valid
            if not vl and not vr:
                l+=1
                r-=1
                continue
            if not vl:
                l+=1
                continue
            if not vr:
                r-=1
                continue
            
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True



        