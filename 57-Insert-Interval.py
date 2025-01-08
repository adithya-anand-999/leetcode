class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if not intervals: return [newInterval]
        i = 0
        res = []
        n = len(intervals)
        
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i+=1
        
        while i < n and newInterval[1] >= intervals[i][0]: # you stop merging if intervals[i][0] happens after newInterval[1], aka newInterval ending
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1],intervals[i][1])]
            i+=1
        res.append(newInterval)
        res+=intervals[i:]
        return res