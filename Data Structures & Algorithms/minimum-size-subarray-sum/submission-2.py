class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums) + 1
        subarray_sum = 0
        i = 0

        for j in range(len(nums)):
            subarray_sum += nums[j]
            while subarray_sum >= target:
                min_length = min(min_length, j - i + 1)
                subarray_sum -= nums[i]
                i += 1

        return 0 if min_length == len(nums) + 1 else min_length    
                