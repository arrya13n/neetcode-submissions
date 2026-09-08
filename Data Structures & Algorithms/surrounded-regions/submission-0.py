class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        row,cols = len(board),len(board[0])

        def dfs(r,c):
            if r<0 or r >= row or c< 0 or c >= cols or board[r][c] != 'O':
                return
            
            board[r][c] = "A"
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
            
        for r in range(row):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][cols-1] == "O":
                dfs(r,cols-1)
            
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
            if board[row-1][c] == "O":
                dfs(row-1,c)
            
        for r in range(row):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "A":
                    board[r][c] = "O"