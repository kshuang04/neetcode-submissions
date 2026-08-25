class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row, col))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if (r in range(num_rows) and
                        c in range(num_cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):

                        q.append((r, c))
                        visited.add((r, c))


        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    num_islands += 1
        
        return num_islands