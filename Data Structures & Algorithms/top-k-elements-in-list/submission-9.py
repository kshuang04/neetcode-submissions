class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int) # num: count

        for num in nums:
            counts[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)] # index is frequency

        for num, count in counts.items():
            buckets[count].append(num)
        
        result = []
        while k:
            for i in range(len(buckets)-1, -1, -1):
                for num in buckets[i]:
                    result.append(num)
                    if len(result) >= k:
                        return result
        
        return result

