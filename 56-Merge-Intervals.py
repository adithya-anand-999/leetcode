class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        def overlap(inv1,inv2):
            return inv1[1]>=inv2[0]
        
        l = intervals[0]
        res = []

        for r in intervals[1:]:
            if overlap(l,r):
                l = [l[0],max(l[1],r[1])]
            else:
                res.append(l)
                l = r
        return res + [l]