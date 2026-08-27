class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int) # num: count

        for num in nums:
            counts[num] += 1
        
        minHeap = [] # [-count, num] pairs

        for num, count in counts.items():
            minHeap.append([-count, num])
        
        heapq.heapify(minHeap)

        result = []
        for _ in range(k):
            _, num = heapq.heappop(minHeap)
            result.append(num)
        
        return result