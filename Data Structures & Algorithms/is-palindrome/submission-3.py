class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean string
        clean_str = ""
        for c in s:
            if c.isalnum():
                clean_str += c.lower()
                
        # Check palindrome
        i = 0
        j = len(clean_str) - 1

        while i < j:
            if clean_str[i] != clean_str[j]:
                return False
            i += 1
            j -= 1
        
        return True