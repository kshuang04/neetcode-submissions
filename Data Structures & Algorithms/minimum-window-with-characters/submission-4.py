class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # Initialize hashmaps
        count_t = defaultdict(int)
        window = defaultdict(int)

        # Make count_t hashmap
        for c in t:
            count_t[c] += 1
        
        # Initialize have and need
        have = 0
        need = len(count_t)

        # Initialize result
        result = [-1, -1]
        result_len = float("inf")
        l = 0

        # For each character in s ...
        for r in range(len(s)):
            c = s[r]

            # Add curr char in window to window hashmap
            window[c] += 1

            # Check if newly added char meets a condition
            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                # Update result
                if (r - l + 1) < result_len:
                    result_len = r - l + 1
                    result = [l, r]
                
                # Pop from left
                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        
        l, r = result
        return s[l:r+1] if result_len != float("inf") else ""
