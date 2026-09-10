class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # num: count

        for num in nums:
            count[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in count.items():
            buckets[count].append(num)
        
        result = []

        while k > 0:
            for i in range(len(buckets) - 1, -1, -1):
                if buckets[i]:
                    for num in buckets[i]:
                        result.append(num)
                        k -= 1
                        if k == 0:
                            return result
        
        return result