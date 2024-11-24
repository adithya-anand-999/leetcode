class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        # dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        n,m = len(grid),len(grid[0])

        # def help(r,c):
        #     #run a DFS from this r,c
        #     q = deque([(r,c)])
        #     while q:
        #         br,bc = q.popleft()
        #         grid[br][bc] = '0'
        #         for dr,dc in dirs:
        #             nr,nc = br+dr,bc+dc
        #             if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc] == '1':
        #                 q.append((nr,nc))

        def help(r,c):
            if r<0 or r>=n or c<0 or c>=m or grid[r][c] == '0': return
            grid[r][c] = '0'
            help(r+1,c)
            help(r-1,c)
            help(r,c+1)
            help(r,c-1)
            

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    res+=1 #seen a new island
                    help(i,j) #mark all visited 1's as 0's showing they are connected. Doing so makes it to where every 1 I see will signify an unconnected 1 thus a new island. 
        return res
        #The issue is that I am keeping track of all the starts, this leads to using too much memory. Furhter it is unnesesary. Just run your BFS algo to visit islands whenever you see a 1 as you are iterating through the grid, when you see 1 call your function. 

        # starts = []
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == '1':starts.append((i,j))
        
        # visited = set()

        #you want to run a BFS turning each 1 into a visit (either pushing the tuple into a set or just chaing value, chaning value is computatilly easier). You dont add any more things to queue, you have already added them at the start that is it. Those are all the ones you added at the start. 


        # for cord in starts:
        #     r,c = cord
        #     if grid[r][c] == '0': continue
        #     res+=1

        #     #run a DFS from this r,c
        #     q = deque([(r,c)])
        #     while q:
        #         br,bc = q.popleft()
        #         grid[br][bc] = '0'
        #         for dr,dc in dirs:
        #             nr,nc = br+dr,bc+dc
        #             if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc] == '1':
        #                 q.append((nr,nc))
        # return res

        # while queue:
        #     curr = queue.popleft()
        #     if curr in visited: continue
        #     res+=1
        #     visited.add(curr)

        #     for dr,dc in dir:
        #         r,c = dr+curr[0], dc+curr[1]
        #         if r>=0 and r<n and c>=0 and c<m and grid[r][c] == '1':
        #             visited.add((r,c))
        #             queue.append((r,c))
        # return res