class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # [temp: index] pairs

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, stack_i = stack.pop()
                result[stack_i] = i - stack_i
            
            stack.append([temp, i])

        return result