"""
200. Number of Islands (Medium)

Description
DFS problem. Recursive or Stack

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        def dfs(i, j):

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return

            grid[i][j] = "0"
            dfs(i + 1, j)  # North
            dfs(i, j + 1)  # East
            dfs(i - 1, j)  # South
            dfs(i, j - 1)  # East

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1

        return cnt


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#
#         r, c = len(grid), len(grid[0])
#         visited = [[False for _ in range(c)] for _ in range(r)]
#         island = 0
#
#         for i in range(r):
#             for j in range(c):
#                 if grid[i][j] == "1" and not visited[i][j]:
#                     stack = [(i, j)]
#                     while stack:
#                         x, y = stack.pop()
#                         visited[x][y] = True
#                         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                             nx, ny = x + dx, y + dy
#                             if (0 <= nx < r) and (0 <= ny < c) and grid[nx][ny] == "1" and not visited[nx][ny]:
#                                 stack.append((nx, ny))
#                     island += 1
#         return island

