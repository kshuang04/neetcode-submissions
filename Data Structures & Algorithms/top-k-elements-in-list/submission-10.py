class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int) # nums: count

        for num in nums:
            hashmap[num] += 1
        
        buckets = [[] for i in range(len(nums) + 1)] # index is count

        for num, count in hashmap.items():
            buckets[count].append(num)
        
        result = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) >= k:
                    return result
        
        return result