class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")":"(",
            "]":"[",
            "}":"{",
        }

        stack = []

        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif c in pairs:
                if stack:
                    top = stack.pop()
                    if pairs[c] != top:
                        return False
                else:
                    return False
        
        return False if stack else True
