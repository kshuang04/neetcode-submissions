class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for character in s:
            if character.isalnum():
                clean_str += character.lower()

        p1 = 0
        p2 = len(clean_str) - 1

        while p1 < p2:
            if clean_str[p1] != clean_str[p2]:
                return False
            
            p1 += 1
            p2 -= 1
            
        return True
