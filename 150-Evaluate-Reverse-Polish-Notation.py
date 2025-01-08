class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop()) # no need to check if stack non empty as told to be valid
            elif t == '-':
                r = stack.pop()
                stack.append(stack.pop() - r)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                r = stack.pop()
                stack.append(int(stack.pop() / r))
            else: stack.append(int(t))
        return stack.pop()