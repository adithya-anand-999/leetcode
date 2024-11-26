class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        numFresh, time = 0, -1
        n,m = len(grid),len(grid[0])

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2: q.append((r,c))
                elif grid[r][c] == 1: numFresh+=1
        if not q and numFresh == 0: return 0

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in [(-1,0), (1,0), (0,1), (0,-1)]:
                    nr,nc = r+dr,c+dc
                    if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        numFresh-=1
                        q.append((nr,nc))
            time+=1
        if numFresh>0: return -1
        return time