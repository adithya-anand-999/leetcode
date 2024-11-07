class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prereqs = defaultdict(list)

        # for target,prereq in prerequisites:
        #     if target == prereq: return False
        #     stack = [prereq]
        #     while stack:
        #         curr = stack.pop()
        #         if curr in prereqs:
        #             if target in prereqs[curr]: return False
        #             stack += prereqs[curr]

        #     # if prereq in prereqs and target in prereqs[prereq]:
        #     #     return False
        #     prereqs[target].append(prereq)
        # return True
            # else:
        prereqs = defaultdict(list)
        for target,prereq in prerequisites:
            prereqs[target].append(prereq)
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


