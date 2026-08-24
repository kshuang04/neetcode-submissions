class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bSearch(leftBias): # leftBias = True when want to find the starting position
            l = 0
            r = len(nums) - 1
            i = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    i = mid
                    if leftBias:
                        r = mid - 1
                    else:
                        l = mid + 1
            
            return i
        
        start = bSearch(True)
        end = bSearch(False)
        return [start, end]
