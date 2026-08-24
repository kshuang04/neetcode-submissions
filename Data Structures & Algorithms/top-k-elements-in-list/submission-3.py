class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int) # num: frequency

        for num in nums:
            counts[num] += 1
        
        maxHeap = []

        for num, freq in counts.items():
            maxHeap.append([-freq, num])
        
        heapq.heapify(maxHeap)

        result = []
        for _ in range(k):
            _, num = heapq.heappop(maxHeap)
            result.append(num)
        
        return result