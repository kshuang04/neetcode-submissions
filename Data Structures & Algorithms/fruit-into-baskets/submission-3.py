class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int) # fruit type: count in basket
        l = 0
        max_fruit = 0
        curr_total = 0

        for r in range(len(fruits)):
            counts[fruits[r]] += 1
            curr_total += 1
            
            while len(counts) > 2:
                counts[fruits[l]] -= 1
                curr_total -= 1
                if counts[fruits[l]] == 0:
                    counts.pop(fruits[l])
                l += 1

            max_fruit = max(max_fruit, curr_total)
        
        return max_fruit