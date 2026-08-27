class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = -1
        seen = set()
        l = 0

        for r in range(len(s)):
            while s[r] in seen and l <= r:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_length = max(max_length, len(seen))
        
        return max_length if max_length != -1 else 0
            