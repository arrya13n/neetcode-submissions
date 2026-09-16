class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        if not board:
            return True

        def dfs(r,c,i):
            #base case
            if i == len(word):
                return True
            if (0 > r or r >= rows) or (0 > c  or c >= cols) or board[r][c] != word[i] or board[r][c] == '#':
                return False
            
            board[r][c] = '#'
            result = (dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1))
            board[r][c] = word[i]

            return result
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False