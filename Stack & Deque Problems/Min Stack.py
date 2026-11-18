class MinStack:

    def __init__(self):

        self.stack = []
        self.cur_min = float("inf")
        self.min_history = []

    def push(self, value: int) -> None:

        self.min_history.append(self.cur_min)
        self.cur_min = min(self.cur_min, value)
        self.stack.append(value)

    def pop(self) -> None:
        self.cur_min = self.min_history.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:

        return self.cur_min
