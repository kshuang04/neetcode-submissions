class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []
        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif c in pairs:
                if not stack:
                    return False
                if stack.pop() != pairs[c]:
                    return False

        return not stack