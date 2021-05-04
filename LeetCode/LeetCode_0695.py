"""
695. Max Area of Island (medium)

1) use dfs
2) check the visiting point
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        r, c = len(grid), len(grid[0])
        sol = 0
        stack = []
        visited = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if (grid[i][j] == 1) and (visited[i][j] == 0):  # starting point of island
                    stack.append((i, j))
                    visited[i][j] = 1
                    area = 0
                    while stack:
                        x, y = stack.pop()
                        # visited[x][y] = 1 => stack can get the duplicated coordinates
                        area += 1

                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if (0 <= nx < r) and (0 <= ny < c) and (grid[nx][ny] == 1) and (visited[nx][ny] == 0):
                                stack.append((nx, ny))
                                visited[nx][ny] = 1
                    sol = max(sol, area)
        return sol