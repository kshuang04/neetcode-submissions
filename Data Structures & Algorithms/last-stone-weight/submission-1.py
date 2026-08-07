class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0
        
        stones.sort()
        result = stones.pop() - stones.pop()

        if result > 0:
            stones.append(result)

        return self.lastStoneWeight(stones)