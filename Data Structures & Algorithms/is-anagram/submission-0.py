class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_set = {}

        for char in s:
            if char not in hash_set:
                hash_set[char] = 1
            else:
                hash_set[char] += 1
        
        for char in t:
            if char in hash_set:
                hash_set[char] -= 1
            else:
                return False
        
        for count in hash_set.values():
            if count != 0:
                return False

        return True
        