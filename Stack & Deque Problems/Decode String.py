class Solution:
    def decodeString(self, s: str) -> str:

        nums = []
        chars = []
        num = 0

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                nums.append(num)
                chars.append("[")
                num = 0

            elif ch == "]":
                cur = []

                while chars[-1] != "[":
                    cur.append(chars.pop())

                chars.pop()

                decoded = "".join(reversed(cur))

                chars.append(nums.pop() * decoded)

            else:
                chars.append(ch)

        return "".join(chars)
