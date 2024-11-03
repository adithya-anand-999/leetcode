class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = list(a),list(b)
        la = len(a)
        lb = len(b)
        if la < lb:
            a = ['0']*abs(la-lb) + a
        elif lb < la:
            b = ['0']*abs(la-lb) + b
        print(a,b)

        carry = 0
        for i in range(len(a)-1, -1, -1):
            sum = carry + int(a[i]) + int(b[i])
            if sum == 0:
                b[i] = '0'
            elif sum == 1:
                b[i] = '1'
                carry = 0
            elif sum == 2:
                b[i] = '0'
                carry = 1
            else:
                b[i] = '1'
                carry = 1
        return ''.join(b) if carry == 0 else ''.join(['1']+b)