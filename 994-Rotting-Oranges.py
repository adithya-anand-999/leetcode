class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        starts = deque([])
        m,n = len(grid),len(grid[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: fresh+=1
                elif grid[r][c] == 2: starts.append((r,c))
        
        if not starts and fresh>0: return -1

        while starts:
            num = len(starts)
            for _ in range(num):
                r,c = starts.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc
                    if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        starts.append((nr,nc))
                        fresh-=1
            if starts: time+=1
        
        return time if fresh==0 else -1