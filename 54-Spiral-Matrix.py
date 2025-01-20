class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # right, down, left, up
        # dont re-add already seen elements
        # if you see an element already seen or element is out of bounds switch to next direction
        # check if element is valid before adding it, if its not valid then break
        # you can %4 to alternate within the diretions
        # its all r,c order

        #append value at r,c
        #get new r,c by applying the dir
        #if new r,c is in visited then apply the next direction
        #if the new new r,c is in visited (break)
        #if we dont break then set new values 

        #when to check if in bounds, being out of bounds is also a reason to switich directions. But only for first switch. 

        if not matrix: return []
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0
        r,c = 0,0
        m,n = len(matrix),len(matrix[0])
        visited = set()
        res = []

        while True:
            # print(r,c)
            res.append(matrix[r][c])
            visited.add((r,c))
            nr,nc = r+dirs[d%4][0],c+dirs[d%4][1]
            if nr<0 or nr>=m or nc<0 or nc>=n or (nr,nc) in visited:
                d+=1
                nr,nc = r+dirs[d%4][0],c+dirs[d%4][1]
                if nr<0 or nr>=m or nc<0 or nc>=n or (nr,nc) in visited: break
            r,c = nr,nc
        return res
