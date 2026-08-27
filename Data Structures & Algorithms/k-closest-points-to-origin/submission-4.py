class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # [distance, x, y] triplets
        for x, y in points:
            minHeap.append([x**2 + y**2, x, y])
        
        heapq.heapify(minHeap)

        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            result.append([x, y])
        return result