class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l,r = 0,len(self.storage[key])-1
        if r == -1: return ""
        while l<=r:
            m = (l+r)//2
            val = self.storage[key][m]
            if val[0] == timestamp:
                return val[1]
            if val[0] < timestamp:
                l = m+1
            else:
                r = m-1
        return self.storage[key][r][1] if self.storage[key][r][0] <= timestamp else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)