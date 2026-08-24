class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_islands = 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            visited.add((row, col))
            
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(num_rows) and
                        c in range(num_cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):

                        q.append((r, c))
                        visited.add((r, c))

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    num_islands += 1
        
        return num_islands
