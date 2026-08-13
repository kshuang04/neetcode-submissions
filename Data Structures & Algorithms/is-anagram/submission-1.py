class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {} # character : number of occurences
        for c in s:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1
        
        for c in t:
            if c in hash_map:
                hash_map[c] -= 1
            else:
                return False
        
        for n in hash_map.values():
            if n != 0:
                return False
        
        return True