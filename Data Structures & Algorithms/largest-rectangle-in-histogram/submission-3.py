class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, index) pairs
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                stack_h, stack_i = stack.pop()
                max_area = max(max_area, stack_h * (i - stack_i))
                start = stack_i
            stack.append((h, start))
        
        for h, i in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area