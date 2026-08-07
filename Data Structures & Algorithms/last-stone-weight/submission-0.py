class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0
        
        stones.sort()
        result = stones[-1] - stones[-2]
        if result == 0:
            stones.pop()
            stones.pop()
        else:
            stones.pop()
            stones[-1] = result

        return self.lastStoneWeight(stones)