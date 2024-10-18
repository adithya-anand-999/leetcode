class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(', '{', '[']
        closes = [')', '}', ']']

        for c in s:
            if c in opens:
                stack.append(c)
            elif c in closes:
                #if trying to pop you have to make sure the stack is not empty. 
                if not stack or opens[closes.index(c)] != stack.pop():
                    return False
        return not stack
