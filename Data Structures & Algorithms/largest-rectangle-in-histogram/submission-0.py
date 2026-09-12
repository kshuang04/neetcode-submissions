class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (index, height) pairs

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                stack_i, stack_h = stack.pop()
                max_area = max(max_area, stack_h * (i - stack_i))
                start = stack_i
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area