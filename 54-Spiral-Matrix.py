class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0
        m,n = len(matrix),len(matrix[0])
        res = []
        r,c = 0,0
        visited = set()

        while True:
            res.append(matrix[r][c])
            visited.add((r,c))
            nr,nc = r+dirs[d%4][0],c+dirs[d%4][1]

            if nr<0 or nr>=m or nc<0 or nc>=n or (nr,nc) in visited:
                d+=1
                nr,nc = r+dirs[d%4][0],c+dirs[d%4][1]
                if nr<0 or nr>=m or nc<0 or nc>=n or (nr,nc) in visited:
                    break
            r,c = nr,nc
        return res
                