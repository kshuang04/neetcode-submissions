class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int) # fruit type: count in basket
        l = 0
        curr_total = 0
        max_fruit = 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            curr_total += 1

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                curr_total -= 1
                if not count[f]:
                    count.pop(f)
                l += 1

            max_fruit = max(max_fruit, curr_total)
        
        return max_fruit