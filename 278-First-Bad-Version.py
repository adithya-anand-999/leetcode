# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1,n

#If the current mid is bad, that means we have to check before (so less than mid), if current version is good we have to check past it as it means we still have not found the first bad version. 
        while l <= r:
            mid = (l+r)//2

            if isBadVersion(mid):
                r = mid-1
            else:
                l = mid+1
#Why is returning l correct and not r. r comes out to be 1 more than expected answer. 
        return l