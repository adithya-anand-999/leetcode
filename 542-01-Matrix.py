class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        starts = deque([])
        m,n = len(mat),len(mat[0])
        max_val = m*n+1
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    starts.append((r,c))
                else:
                    mat[r][c] = max_val
        
        while starts:
            r,c = starts.popleft()
            val = mat[r][c]
            for dr,dc in dirs:
                fr,fc = r+dr,c+dc
                if fr>=0 and fr<m and fc>=0 and fc<n and mat[fr][fc] > val+1:
                    starts.append((fr,fc))
                    mat[fr][fc] = val+1
        return mat
