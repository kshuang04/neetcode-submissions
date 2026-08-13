class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "}":"{", "]":"["}
        stack = []

        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if stack:
                    top = stack.pop()
                    if top != pairs[c]:
                        return False
                else:
                    return False
        
        return not stack
