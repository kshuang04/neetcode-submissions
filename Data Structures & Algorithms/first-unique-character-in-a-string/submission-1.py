class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = defaultdict(int) # character: frequency

        for c in s:
            hash_map[c] += 1
        
        for i, c in enumerate(s):
            if hash_map[c] == 1:
                return i
        
        return -1