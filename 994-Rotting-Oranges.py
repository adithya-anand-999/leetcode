class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        n,m = len(grid), len(grid[0])
        time = 0 # 1 or 0
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        num_fresh = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    num_fresh+=1

        if num_fresh == 0: return 0
        
        while rotten:
            initial_rotten = len(rotten)
            for i in range(initial_rotten):
                r,c = rotten.popleft()
                for dr,dc in dirs:
                    fr,fc = dr+r,dc+c
                    if fr >= 0 and fr < n and fc >= 0 and fc < m and grid[fr][fc] == 1:
                        num_fresh-=1
                        grid[fr][fc] = 2
                        rotten.append((fr,fc))
            if rotten: time+=1 # This means we have rotted something so we increment time, else nothing new rotten so prev time state equal to curr time state. 

        
        return time if num_fresh == 0 else -1
                    
