"""
    994. Rotting Oranges
    https://leetcode.com/problems/rotting-oranges/
"""

from collections import deque  # Using double-ended queue


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        empty, fresh, rotten = 0, 1, 2  # default enums
        m = len(grid)
        n = len(grid[0])

        fresh_counter = 0
        rotten_q = deque()  # rotten queue

        for i in range(m):
            for j in range(n):
                if grid[i][j] == fresh:
                    fresh_counter += 1  # count fresh oranges
                elif grid[i][j] == rotten:
                    rotten_q.append((i, j))  # enqueue rotten oranges

        if fresh_counter == 0:
            return 0  # if no fresh oranges, return 0

        num_minutes = -1

        while rotten_q:
            q_size = len(rotten_q)
            num_minutes += 1  # increment minutes
            for _ in range(q_size):
                i, j = (
                    rotten_q.popleft()
                )  # pop first rotten orange because it is the first to rot

                for row, col in [
                    (i, j + 1),
                    (i, j - 1),
                    (i + 1, j),
                    (i - 1, j),
                ]:  # check adjacent oranges

                    if (
                        row >= 0
                        and col >= 0
                        and row < m
                        and col < n
                        and grid[row][col] == fresh
                    ):  # if adjacent orange is fresh
                        grid[row][col] = rotten  # mark it as rotten
                        rotten_q.append((row, col))
                        fresh_counter -= 1  # decrement fresh oranges

        if fresh_counter == 0:
            return num_minutes  # if no fresh oranges, return minutes
        else:
            return -1  # return -1 if there are still fresh oranges


print(Solution().orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(Solution().orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(Solution().orangesRotting(grid=[[0, 2]]))
