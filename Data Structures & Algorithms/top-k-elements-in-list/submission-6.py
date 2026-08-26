class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        minHeap = [] # list of pairs (count, num)

        for num, freq in count.items():
            minHeap.append([freq, num])
        
        minHeap.sort(reverse=True)

        result = []
        for i in range(k):
            result.append(minHeap[i][1])
        
        return result
