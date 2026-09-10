class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # num: count

        for num in nums:
            count[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in count.items():
            buckets[count].append(num)
        
        result = []

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) >= k:
                    return result
        
        return result