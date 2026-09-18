class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        amount = 0

        l = 0
        r = len(height) - 1

        maxL = height[l]
        maxR = height[r]

        while l < r:
            if height[l] <= height[r]:
                l += 1
                maxL = max(maxL, height[l])
                amount += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                amount += maxR - height[r]
        
        return amount
