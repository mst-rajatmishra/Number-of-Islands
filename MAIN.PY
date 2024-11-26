class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            # Check boundaries and if the cell is land
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return
            # Mark the current cell as visited
            grid[i][j] = '0'
            # Visit all adjacent cells (up, down, left, right)
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        island_count = 0
        
        # Traverse the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # Found an unvisited land cell
                    island_count += 1
                    dfs(i, j)  # Perform DFS to mark all the connected land cells as visited
        
        return island_count
