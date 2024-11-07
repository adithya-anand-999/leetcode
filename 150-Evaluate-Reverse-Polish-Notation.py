class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                r = stack.pop()
                stack.append(stack.pop() - r)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                r = stack.pop()
                stack.append(int(stack.pop()/r))
            else: stack.append(int(c))
        return stack.pop()