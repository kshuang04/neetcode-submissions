class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruit = 0

        for i in range(len(fruits)):
            seen = set()
            curr_max = 0
            for j in range(i, len(fruits)):
                if fruits[j] not in seen:
                    if len(seen) < 2:
                        seen.add(fruits[j])
                    else:
                        break
                curr_max += 1
            max_fruit = max(max_fruit, curr_max)
        
        return max_fruit
                