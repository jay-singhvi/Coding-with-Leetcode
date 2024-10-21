"""
    200. Number of Islands
    https://leetcode.com/problems/number-of-islands/
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        island_count = 0
        m = len(grid)  # Horizontal Length of Matrix
        n = len(grid[0])  # Vertical Length of Matrix

        def dfs(i, j):
            # Not out of bounds and is a land
            if i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == "1":
                grid[i][j] = "0"

                # check all 4 directions if there are any islands
                dfs(i, j + 1)
                dfs(i, j - 1)
                dfs(i + 1, j)
                dfs(i - 1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island_count += 1  # increment only for new islands
                    dfs(i, j)  # marks lands as water to avoid repetitions

        return island_count


print(
    Solution().numIslands(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)

print(
    Solution().numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
