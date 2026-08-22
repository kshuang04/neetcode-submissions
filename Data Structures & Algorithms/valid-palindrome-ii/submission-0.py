class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Check if already palindrome
        if self.isPalindrome(s):
            return True
        
        # Remove characters and check
        for i in range(len(s)):
            str_slice = s[:i] + s[i+1:]
            
            if self.isPalindrome(str_slice):
                return True
        
        return False


    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True