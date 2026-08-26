"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        hashmap = defaultdict(int) # time: number of meetings

        for interval in intervals:
            for i in range(interval.start, interval.end):
                hashmap[i] += 1
        
        return max(hashmap.values())