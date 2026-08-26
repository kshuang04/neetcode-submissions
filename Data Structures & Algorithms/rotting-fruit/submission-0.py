class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        num_fresh = 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    num_fresh += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while num_fresh > 0:
            update = False
            for i in range(num_rows):
                for j in range(num_cols):
                    if grid[i][j] == 2:
                        for dr, dc in directions:
                            r = i + dr
                            c = j + dc

                            if (r in range(num_rows) and c in range(num_cols) and grid[r][c] == 1):
                                grid[r][c] = 3
                                num_fresh -= 1
                                update = True
            
            if not update:
                return -1

            for i in range(num_rows):
                for j in range(num_cols):
                    if grid[i][j] == 3:
                        grid[i][j] = 2
            
            minutes += 1

        return minutes