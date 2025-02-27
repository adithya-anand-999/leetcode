class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals: return ""
        vals = self.vals[key]
        l,r = 0,len(vals)-1

        while l<=r:
            mid = (l+r)//2
            if vals[mid][0] == timestamp: return vals[mid][1]
            if vals[mid][0] > timestamp: r = mid-1
            else: l = mid+1
        return vals[r][1] if r>=0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)