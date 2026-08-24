class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            visited.add((row,col))
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
                        visited.add((r,c))

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    num_islands += 1
        
        return num_islands