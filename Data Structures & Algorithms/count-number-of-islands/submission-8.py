class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            visited.add((i, j))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if (r in range(num_rows) and
                        c in range(num_cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):

                        visited.add((r, c))
                        q.append((r, c))

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    num_islands += 1
                    bfs(i, j)
        
        return num_islands