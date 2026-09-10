class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        
        return True if len(temp) != len(nums) else False