class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if intervals == []: return [newInterval]
        res = []
        i = 0

        while i < len(intervals) and intervals[i][1]  <  newInterval[0]:
            res.append(intervals[i])
            i+=1
        #the below line shows up as out of range. 
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]),
                            max (intervals[i][1], newInterval[1])]
            i+=1
        res.append(newInterval)
        res += intervals[i:]
        return res