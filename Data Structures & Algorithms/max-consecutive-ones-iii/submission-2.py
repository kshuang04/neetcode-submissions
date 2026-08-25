class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_count = 0
        curr_count = 0
        flips = k

        for r in range(len(nums)):
            if nums[r] == 0:
                while not flips and l <= r:
                    curr_count -= 1
                    if nums[l] == 0:
                        flips += 1
                    l += 1
                flips -= 1
            
            curr_count += 1
            max_count = max(max_count, curr_count)
        
        return max_count