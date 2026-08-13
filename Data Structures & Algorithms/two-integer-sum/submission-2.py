class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # number : index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hash_map:
                return [hash_map[complement], i]
            else:
                hash_map[num] = i