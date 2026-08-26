"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        intervals.sort(key=lambda x: x.start)
        schedule = [intervals[0]]

        for interval in intervals[1:]:
            last_end = schedule[-1].end
            if interval.start < last_end:
                return False
            schedule.append(interval)
        
        return True
