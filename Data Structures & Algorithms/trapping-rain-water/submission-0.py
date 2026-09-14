class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        mins = [0] * n
        result = [0] * n

        for i in range(n):
            maxLeft[i] = max(height[i], maxLeft[i - 1] if (i - 1) >= 0 else 0)
        
        for i in range(n - 1, -1, -1):
            maxRight[i] = max(height[i], maxRight[i + 1] if (i + 1) < len(height) else 0)
        
        for i in range(n):
            mins[i] = min(maxLeft[i], maxRight[i])
        
        for i in range(n):
            result[i] = max(mins[i] - height[i], 0)
        
        return sum(result)