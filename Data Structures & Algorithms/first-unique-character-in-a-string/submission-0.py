class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {} # character: frequency

        for c in s:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1

        for i, c in enumerate(s):
            if hash_map[c] == 1:
                return i
        
        return -1