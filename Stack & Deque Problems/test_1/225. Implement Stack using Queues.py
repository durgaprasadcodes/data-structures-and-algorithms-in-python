from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()
        self.last_appended = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self.last_appended = x

    def pop(self) -> int:
        for num in range(len(self.q) - 1):
            num = self.q.popleft()
            self.q.append(num)
            self.last_appended = num
        return self.q.popleft()

    def top(self) -> int:
        return self.last_appended

    def empty(self) -> bool:
        return not self.q
