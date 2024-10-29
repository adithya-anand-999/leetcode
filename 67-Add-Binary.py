class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a = list(a)
        b = list(b)
        longer,shorter = (a,b) if len(a) > len(b) else (b,a)

        shorter = [0]*(len(longer)-len(shorter)) + shorter

        for i in range(len(shorter)-1,-1,-1):
            val = int(shorter[i]) + int(longer[i]) + carry
            if val == 0:
                shorter[i] = '0'
                carry = 0
            elif val == 1:
                shorter[i] = '1'
                carry = 0
            elif val == 2:
                shorter[i] = '0'
                carry = 1
            else:
                shorter[i] = '1'
                carry = 1  
        shorter = ''.join(shorter)
        if carry == 1: shorter = '1'+shorter
        return shorter

