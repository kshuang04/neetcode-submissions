class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        count_t = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            count_t[c] += 1
        
        have = 0
        need = len(count_t)
        l = 0

        result = ""
        result_len = float("inf")

        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < result_len:
                    result_len = r - l + 1
                    result = s[l:r+1]

                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                
                l += 1
        
        return result if result_len != float("inf") else ""


