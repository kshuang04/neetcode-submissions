class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    result.append([a, nums[l], nums[r]])
                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
        
        return result