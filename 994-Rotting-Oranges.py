class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        num_fresh = 0
        time = 0
        starts = deque([])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: num_fresh+=1
                elif grid[r][c] == 2: starts.append((r,c))
        
        # if not starts: return -1
        if num_fresh == 0: return 0

        while starts:
            rotten_number = len(starts)
            for _ in range(rotten_number):
                r,c = starts.popleft()
                for dr,dc in dirs:
                    fr,fc = r+dr,c+dc
                    if fr>=0 and fr<m and fc>=0 and fc<n and grid[fr][fc] == 1:
                        grid[fr][fc] = 2
                        num_fresh-=1
                        starts.append((fr,fc))
            if starts: time+=1
        return time if num_fresh == 0 else -1
