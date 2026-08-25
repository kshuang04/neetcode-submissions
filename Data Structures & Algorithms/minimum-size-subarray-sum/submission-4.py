class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        min_length = len(nums) + 1
        curr_sum = 0

        for j in range(len(nums)):
            curr_sum += nums[j]
            while curr_sum >= target:
                min_length = min(min_length, j - i + 1)
                curr_sum -= nums[i]
                i += 1
        
        return 0 if min_length == len(nums) + 1 else min_length