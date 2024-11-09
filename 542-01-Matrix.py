class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        starts = deque()
        m,n = len(mat), len(mat[0])
        max_val = m*n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0: starts.append((i,j))
                else: mat[i][j] = max_val
        
        while starts:
            row,col = starts.popleft()

            dir = [(-1,0), (0,-1), (1,0), (0,1)]
            for dr,dc in dir:
                r,c = row+dr,col+dc
                if 0<= r < m and 0<= c < n and mat[r][c] > 1+mat[row][col]:
                    mat[r][c] = 1+mat[row][col]
                    starts.append((r,c))

        return mat            