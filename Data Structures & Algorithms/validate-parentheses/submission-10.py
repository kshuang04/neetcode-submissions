class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        stack = []

        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif c in pairs:
                if stack:
                    top = stack.pop()
                    if top != pairs[c]:
                        return False
                else:
                    return False
        
        return not stack