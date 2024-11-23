class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for tar,pre in prerequisites:
            prereqs[tar].append(pre)
        
        visited = set()
        path = set()

        def dfs(crs):
            if crs in visited: return True
            if crs in path: return False

            path.add(crs)
            for c in prereqs[crs]:
                if not dfs(c): return False
            path.remove(crs)
            visited.add(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True