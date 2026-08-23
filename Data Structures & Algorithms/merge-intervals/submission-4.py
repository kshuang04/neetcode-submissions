class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals
        intervals = sorted(intervals, key= lambda x : x[0])

        # Initialize result list
        result = [intervals[0]]

        # Add intervals to result
        for interval in intervals[1:]:
            last_end = result[-1][1]
            if interval[0] <= last_end:
                result[-1][1] = max(last_end, interval[1])
            else:
                result.append([interval[0], interval[1]])
        
        return result