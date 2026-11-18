class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for ch in operations:
            if ch == "C":
                stack.pop()
            elif ch == "+":
                stack.append(stack[-2] + stack[-1])
            elif ch == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(ch))
        return sum(stack)
