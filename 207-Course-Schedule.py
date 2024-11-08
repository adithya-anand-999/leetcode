class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for crs,pre in prerequisites:
            prereqs[crs].append(pre)
        
        visited = set()
        path = set()
        def dfs(node):
            if node in visited: return True
            if node in path: return False

            path.add(node)
            for n in prereqs[node]:
                if not dfs(n): return False
            path.remove(node)
            visited.add(node)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True