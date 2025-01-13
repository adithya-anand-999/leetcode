class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        count = 0
        
        def help(r,c):
            grid[r][c] = '0'
            for dr,dc in dirs:
                fr,fc = dr+r,dc+c
                if fr>=0 and fr<m and fc>=0 and fc<n and grid[fr][fc] == '1':
                    help(fr,fc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count+=1
                    help(i,j)
        return count