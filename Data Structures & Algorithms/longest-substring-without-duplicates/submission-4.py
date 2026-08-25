class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        seen = set()
        max_length = 0

        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            max_length = max(max_length, len(seen))
        
        return max_length