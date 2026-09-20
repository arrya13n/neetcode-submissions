"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_arr = sorted([i.start for i in intervals])
        end_arr = sorted([i.end for i in intervals])

        str_pt,end_pt = 0,0
        result,count = 0,0

        while str_pt < len(intervals):
            if start_arr[str_pt] < end_arr[end_pt]:
                count += 1
                str_pt += 1
            else:
                count -= 1
                end_pt += 1
            result = max(result, count)
        return result