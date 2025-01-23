class Solution:
    def myAtoi(self, s: str) -> int:
        r = 0
        n = len(s)
        pos = True
        valid = '0123456789'

        while r<n and s[r] == ' ':r+=1

        if r<n and s[r] == '-':
            pos = False
            r+=1
        elif r<n and s[r] == '+':
            r+=1
        
        while r<n and s[r] == '0':r+=1
        
        l = r
        while r<n and s[r] in valid: r+=1

        if r-l>0:
            num = int(s[l:r]) if pos else -int(s[l:r])
            if num > 2147483647: return 2147483647
            if num < -2147483648: return -2147483648
            return num
        else:
            return 0


