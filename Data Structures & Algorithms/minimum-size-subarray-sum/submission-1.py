class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        seen_sum = 0
        i = 0

        for j in range(len(nums)):
            seen_sum += nums[j]
            while seen_sum >= target:
                min_length = min(min_length, j - i + 1)
                seen_sum -= nums[i]
                i += 1
        
        return 0 if min_length == float("inf") else min_length
