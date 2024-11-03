class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # print(s)
        valid = 'abcdefghijklmnopqrstuvwxyz0123456789'
        conFlag = False

        l,r = 0,len(s)-1
        while l<r:
            if s[l] not in valid:
                l+=1
                conFlag = True
            if s[r] not in valid:
                r-=1
                conFlag = True
            if conFlag:
                conFlag = False
                continue
            if s[l] != s[r]:return False
            l+=1
            r-=1
        return True