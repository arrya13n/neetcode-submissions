class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        rows,cols = len(grid),len(grid[0])
        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c,0))
        if not q:
            return
        
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            R,C,distance = q.popleft()
            
            for dr,dc in direction:
                ROW = dr + R
                COL = dc + C

                if (0 <= ROW < rows) and (0 <= COL < cols) and grid[ROW][COL] == INF:
                    grid[ROW][COL] = distance + 1
                    q.append((ROW,COL, distance + 1))
        return