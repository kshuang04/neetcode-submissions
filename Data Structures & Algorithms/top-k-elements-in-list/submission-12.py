class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = [] # (-frequency, num) pairs

        count = defaultdict(int) # num: count

        for num in nums:
            count[num] += 1
        
        for num, freq in count.items():
            maxHeap.append((-freq, num))
        
        heapq.heapify(maxHeap)

        result = []

        for _ in range(k):
            _, num = heapq.heappop(maxHeap)
            result.append(num)
        
        return result