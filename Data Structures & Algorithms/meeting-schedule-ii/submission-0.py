"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = {} # time: num of meetings

        for interval in intervals:
            for i in range(interval.start, interval.end):
                if i not in rooms:
                    rooms[i] = 1
                else:
                    rooms[i] += 1
        
        num_rooms = 0

        for num in rooms.values():
            if num > num_rooms:
                num_rooms = num

        return num_rooms