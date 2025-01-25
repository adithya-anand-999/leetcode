class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c,idx):
            if idx == len(word): return True

            if (r<0 or r>=m or c<0 or c>=n or board[r][c] != word[idx] 
            or (r,c) in visited): 
                return False
            
            visited.add((r,c))

            for dr,dc in dirs:
                if dfs(r+dr, c+dc, idx+1): return True
            
            visited.remove((r,c))
            return False
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    visited = set()
                    if dfs(r,c,0): 
                        return True
        return False