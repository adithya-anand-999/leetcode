class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for crs,pre in prerequisites:
            courses[crs].append(pre)
        
        path = set()
        visited = set()
        def dfs(crs):
            if crs in path: return False
            if crs in visited: return True

#this is not a crs on the current path and we have not seen it before, so we are going to see it
#its on the current path so add it to path            
            path.add(crs)
#we visit by checking each of its prereqs            
            for pre in courses[crs]:
#if any prereq return False then we should return False, return False if we end up at a node seen on the current dfs path
                if not dfs(pre): return False
#the crs is good, so remove from the path and add it to visited as its good
            path.remove(crs)
            visited.add(crs)
#the course is good so we return Ture
            return True
        for crs in range(numCourses):
#If any course returns false then we return false             
            if not dfs(crs): return False
        return True