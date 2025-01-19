class Solution:
    def myAtoi(self, s: str) -> int:
        pos = True
        r = 0
        n = len(s)
        # res = 0
        valid = '0123456789'

#whitespace
        while r<n and s[r].isspace(): r+=1
        
#sign
        if r<n and s[r] == '-': 
            pos = False
            r+=1
        elif r<n and s[r] == '+': r+=1

#leading 0   
        while r<n and s[r] == '0': r+=1

        l = r
#char check
        while r<n and s[r] in valid: r+=1

        if abs(l-r) > 0:
            num = int(s[l:r]) if pos else -int(s[l:r])
            if num > 2147483647: return 2147483647
            if num < -2147483648: return -2147483648
            return num
        else:
            return 0
