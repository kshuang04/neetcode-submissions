class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s: str):
            i = 0
            j = len(s) - 1

            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True


        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return checkPalindrome(s[:i] + s[i+1:]) or checkPalindrome(s[:j] + s[j+1:])
            i += 1
            j -= 1
        
        return True