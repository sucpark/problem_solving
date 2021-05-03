"""
200. Number of Islands (medium)

1) BFS

"""

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row, col = len(grid), len(grid[0])
        cnt = 0

        check = [[0] * col] * row
        # print(check)
        q = deque()

        for i in range(row):
            for j in range(col):
                if (grid[i][j] == "1") and (check[i][j] == 0):  # starting point of island
                    q.append((i, j))
                    print(f"i:{i}, j:{j}, land:{grid[i][j]}, visited:{check[i][j]}")
                    check[i][j] = 1
                    print(f"{i} and {j} are visited")
                    while q:
                        x, y = q.popleft()
                        for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
                            xx = x + dx
                            yy = y + dy
                            print(f"i:{i}, j:{j}, ix:{xx}, jy:{yy}")
                            if (0 <= xx < row) and (0 <= yy < col):
                                print(f"i:{i}, j:{j}, ix:{xx}, jy:{yy}, land:{grid[xx][yy]}, visited:{check[xx][yy]}")
                                if (grid[xx][yy] == '1') and (check[xx][yy] == 0):
                                    # print('survive', x,y,xx, yy)
                                    q.append((xx, yy))
                                    check[xx][yy] = 1
                                    print(f"{xx} and {yy} are visited")
                    cnt += 1

        return cnt
