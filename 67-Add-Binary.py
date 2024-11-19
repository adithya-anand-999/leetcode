class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = list(a),list(b)
        la,lb = len(a),len(b)

        if la < lb:
            a = [0]*abs(la-lb) + a
        else:
            b = [0]*abs(la-lb) + b
        
        # print(a,b)
        carry = 0
        for i in range(len(a)-1, -1, -1):
            sum = carry + int(a[i]) + int(b[i])
            if sum == 0:
                a[i] = '0'
            elif sum == 1:
                carry = 0
                a[i] = '1'
            elif sum == 2:
                carry = 1
                a[i] = '0'
            else:
                carry = 1
                a[i] = '1'

        if carry == 1: a = ['1'] + a
        return ''.join(a)