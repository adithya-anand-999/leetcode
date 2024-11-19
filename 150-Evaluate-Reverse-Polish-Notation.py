class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+': stack.append(stack.pop() + stack.pop())
            elif c == '*': stack.append(stack.pop() * stack.pop())
            elif c == '/': 
                right = stack.pop()
                stack.append(int(stack.pop() / right))
            elif c == '-':
                right = stack.pop()
                stack.append(stack.pop() - right)
            else: stack.append(int(c))
        return stack[-1]