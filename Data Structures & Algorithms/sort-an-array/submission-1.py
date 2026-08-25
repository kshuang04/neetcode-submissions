class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)

        result = []
        n = len(nums)
        for _ in range(n):
            result.append(heapq.heappop(nums))
        
        return result