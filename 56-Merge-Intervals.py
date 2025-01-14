class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        
        def overlap(inv1,inv2):
            # if inv1 end [1] >= inv2 start[0]
            # if inv1[0] <= inv2[0]:
            return inv1[1] >= inv2[0] #not enough of a check, will make more robust
            # else:
                # return inv2[1] >= inv1[0]

        l = intervals[0]
        res = []
        for r in intervals[1:]:
            # function which returns True if overalap False otherwise
            # if overlap l becomes the merged interval
            # if no overlap push l to res, l become r
            # stop when no more r to see, so loop 
            # return res
            if overlap(l,r):
                #overlap
                l = [min(l[0],r[0]), max(l[1],r[1])]
            else:
                res.append(l)
                l = r
        return res+[l]

