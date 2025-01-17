class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        def overlap(inv1,inv2):
            return inv1[1] >= inv2[0]
        
        res = [intervals[0]]

        for i in intervals[1:]:
            if overlap(res[-1],i):
                # l = res.pop()
                # res.append([l[0], max(l[1], i[1])])
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res