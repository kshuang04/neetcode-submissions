class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flips = k
        count = 0
        max_count = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                if flips:
                    flips -= 1
                else:
                    while not flips:
                        if nums[l] == 0:
                            flips += 1
                        l += 1
                        count -= 1
                    flips -= 1
            count += 1
            max_count = max(max_count, count)
        
        return max_count
