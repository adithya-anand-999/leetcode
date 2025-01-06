class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(x,y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if grid[y][x] == \1\:
                grid[y][x] = '0'
                for dx,dy in dirs:
                    dfs(x+dx, y+dy)
        
        num_islands = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == \1\:
                    num_islands+=1
                    dfs(x,y)
        return num_islands
