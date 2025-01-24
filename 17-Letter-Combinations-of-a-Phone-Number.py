class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return[]
        res = []
        n = len(digits)
        # I need a mapping of the digit to the letters it corresponds too. 
        # I am going to use len to see which digit I am on, I can index into my mapping by reading the char at index len in digits
        # use a start variable to see which digit to read. But I actually dont need this, a simple loop should suffice. 
        mapping = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
        }

        def help(trace,length):
            if length == n: 
                res.append(''.join(trace))
                return
            
            for c in mapping[int(digits[length])]:
                trace.append(c)
                help(trace,length+1)
                trace.pop()
        help([],0)
        return res

