class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat[0]),len(mat)
        maxVal = 1+(m*n)

        starts = deque([])
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0: starts.append((r,c))
                else: mat[r][c] = maxVal
        
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        while starts:
            r,c = starts.popleft()
            for dr,dc in dir:
                nr,nc = r+dr,c+dc
                if nr>=0 and nr<n and nc>=0 and nc<m and mat[nr][nc] > 1+mat[r][c]:
                    starts.append((nr,nc))
                    mat[nr][nc] = 1+mat[r][c]
        return mat