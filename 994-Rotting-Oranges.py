class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        n,m = len(grid), len(grid[0])
        numFresh = 0
        time = -1
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:q.append((i,j))
                elif grid[i][j] == 1:numFresh+=1
        if not q and numFresh == 0: return 0

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc
                    if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 #make the fresh orange rotten
                        q.append((nr,nc)) #add to our queue for next iteration as it will spread from here
                        numFresh-=1 #decrement number of fresh oranges
            time+=1
        if numFresh>0: return -1
        return time
        #     qLen = len(q)
        #     holder = deque()
        #     while q:
        #         r,c = q.popleft()
        #         for dr,dc in dirs:
        #             nr,nc = r+dr,c+dc
        #             if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc] == 1:
        #                 grid[nr][nc] = 2
        #                 holder.append((nr,nc))
        #                 numFresh-=1
        #     q = holder
        #     time+=1
        # if numFresh > 0: return -1
        # return time