class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['(','[','{']
        closes = [')',']','}']
        stack = []

        for c in s:
            if c in opens: stack.append(c)
            else:
                if not stack or stack.pop() != opens[closes.index(c)]:
                    return False
        return not stack