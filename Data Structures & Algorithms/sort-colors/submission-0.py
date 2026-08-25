class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3 # index represents the colors, value is color's frequency

        for num in nums:
            buckets[num] += 1
        
        index = 0
        for i in range(3):
            while buckets[i]:
                buckets[i] -= 1
                nums[index] = i
                index += 1