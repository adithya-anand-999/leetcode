class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        MAX_VAL = m*n
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0: queue.append((i,j))
                else: mat[i][j] = MAX_VAL
        while queue:
            row,col = queue.popleft()
            dir = [(1,0), (0,1), (-1,0), (0,-1)]
            for dr,dc in dir:
                r,c = row+dr, col+dc
                if 0<=r<m and 0<=c<n and mat[r][c] > 1+mat[row][col]:
                    mat[r][c] = 1+mat[row][col]
                    queue.append((r,c))
        return mat
