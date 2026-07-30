class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                try:
                    if c == ")" and stack[-1] == "(":
                        stack.pop()
                    elif c == "]" and stack[-1] == "[":
                        stack.pop()
                    elif c == "}" and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                except IndexError:
                    return False
        
        if not stack:
            return True
        else:
            return False