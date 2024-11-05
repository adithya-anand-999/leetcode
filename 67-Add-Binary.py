class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = list(a),list(b)
        diff = abs(len(a) - len(b))
        if len(a) < len(b):
            a = ['0']*diff + a
        else:
            b = ['0']*diff + b
        
        carry = 0
        for i in range(len(b)-1,-1,-1):
            sum = int(a[i]) + int(b[i]) + carry
            if sum == 0:
                a[i] = '0'
            elif sum == 1:
                a[i] = '1'
                carry = 0
            elif sum == 2:
                a[i] = '0'
                carry = 1
            else:
                a[i] = '1'
                carry = 1
        # if carry == 1: a = + a
        return ''.join(a) if carry == 0 else str(carry)+''.join(a)