class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = ""
        for ch in s:

            if ch == "(":
                count += 1
                if count > 1:
                    res += "("
            else:
                if count > 1:
                    res += ")"
                count -= 1

        return res
