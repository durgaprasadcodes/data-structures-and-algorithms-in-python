class MinStack:

    def __init__(self):
        self.stack = []
        self.min_history = []

    def push(self, value: int) -> None:
        if self.min_history and self.min_history[-1] < value:
            self.min_history.append(self.min_history[-1])
        else:
            self.min_history.append(value)
        self.stack.append(value)

    def pop(self) -> None:
        self.min_history.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_history[-1]
