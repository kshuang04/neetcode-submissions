class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean string
        clean_str = ""
        for c in s:
            if c.isalnum():
                clean_str += c.lower()

        # check palindrome
        l = 0
        r = len(clean_str) - 1

        while l < r:
            if clean_str[l] != clean_str[r]:
                return False
            l += 1
            r -= 1
        
        return True