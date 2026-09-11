class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        max_length = 0

        for num in nums:
            if (num - 1) not in setNums:
                curr_length = 0

                while (num + curr_length) in setNums:
                    curr_length += 1
                
                max_length = max(max_length, curr_length)
        
        return max_length