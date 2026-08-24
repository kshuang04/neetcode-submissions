class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen = set()
        i = 0

        for c in s:
            while c in seen:
                seen.remove(s[i])
                i += 1
            seen.add(c)
            max_length = max(max_length, len(seen))
        
        return max_length