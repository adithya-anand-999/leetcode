class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if self.min:
            # print(self.min)
            # print(self.min[-1])
            if val < self.min[-1]: self.min.append(val)
            else: self.min.append(self.min[-1])
            # self.min.append(val if val < self.min[-1] else self.min[1])
        else:
            self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()