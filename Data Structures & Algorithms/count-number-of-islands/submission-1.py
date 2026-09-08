class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_island = 0

        if not grid:
            return 0
        
        row,cols = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid [r][c] = '0'
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(row):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    total_island += 1
        return total_island

