class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # num: frequency

        for num in nums:
            count[num] += 1
        
        minHeap = []
        for num, count in count.items():
            minHeap.append((count, num))
        
        heapq.heapify(minHeap)

        largest = heapq.nlargest(k, minHeap)

        result = []
        for freq, num in largest:
            result.append(num)
        
        return result