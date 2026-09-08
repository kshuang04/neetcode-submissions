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
                else:
                    top = stack.pop()
                    if top != pairs[c]:
                        return False
        
        return False if stack else True