class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # num: freq

        for num in nums:
            count[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)] # index is frequency

        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result
        
        return result
