# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        num_Rooms = 0
        available = 0
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()
        
        s = 0
        e = 0
        
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    num_Rooms += 1
                else:
                    available -= 1
                    
                s += 1
            else:
                available += 1
                e += 1
        return num_Rooms