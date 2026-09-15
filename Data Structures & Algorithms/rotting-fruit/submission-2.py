class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        minutes, fresh_oranges = 0,0

        rows,cols = len(grid),len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    q.append([r,c])

        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh_oranges > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in direction:
                    row,col = dr+r,dc+c
                    if (row < 0 or row ==len(grid) or col < 0 or col == len(grid[0]) or grid[row][col]!= 1):
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh_oranges -= 1
            minutes += 1
        return minutes if fresh_oranges == 0 else -1