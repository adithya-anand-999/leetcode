class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        m,n = len(grid),len(grid[0])
        count = 0

        def help(r,c):
            grid[r][c] = '0'
            for dr,dc in dirs:
                nr,nc = dr+r,dc+c
                if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc] == '1':
                    help(nr,nc)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    count+=1
                    help(r,c)
        return count