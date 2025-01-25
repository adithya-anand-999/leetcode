class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return[]
        n = len(digits)
        res = []
        mapping = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        def geko(trace,idx):
            nonlocal n
            if idx == n: 
                res.append(''.join(trace))
                return
            
            for d in mapping[digits[idx]]:
                trace.append(d)
                geko(trace,idx+1)
                trace.pop()
        geko([],0)
        return res