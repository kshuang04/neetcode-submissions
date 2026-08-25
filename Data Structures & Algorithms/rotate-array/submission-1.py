class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # Reverse entire array
        reverse(0, len(nums) - 1)
        
        # Reverse left portion
        reverse(0, k - 1)

        # Reverse right portion
        reverse(k, len(nums) - 1)