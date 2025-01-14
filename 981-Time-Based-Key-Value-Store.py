class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
        vals = self.store[key]
        l,r = 0,len(vals)-1

        # Recursive approach
        while l<=r:
            mid = (l+r)//2
            if vals[mid][0] == timestamp:
                return vals[mid][1]
            if vals[mid][0] > timestamp:
                r = mid-1
            else:
                l = mid+1
        return vals[r][1] if r>=0 else ""

        # Iterative approach is too slow
        # n = len(vals)
        # if n == 1: return vals[0][1]
        # p,c = 0,1
        # while c<n and vals[c][0] <= timestamp: 
        #     p+=1
        #     c+=1
        # return vals[p][1] if vals[p][0] <= timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)