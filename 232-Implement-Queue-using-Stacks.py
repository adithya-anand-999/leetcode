class MyQueue:

    def __init__(self):
        self.queue = []
        self.holder = []

    def push(self, x: int) -> None:
        n = len(self.queue)
        for _ in range(n):
            self.holder.append(self.queue.pop())
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.holder.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()