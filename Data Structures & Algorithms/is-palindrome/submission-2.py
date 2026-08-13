class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""

        for c in s:
            if c.isalnum():
                clean_str += c.lower()
        
        start = 0
        end = len(clean_str) - 1

        while start < end:
            if clean_str[start] != clean_str[end]:
                return False

            start += 1
            end -= 1
        
        return True