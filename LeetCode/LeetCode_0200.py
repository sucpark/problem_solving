"""
200. Number of Islands (medium)

1) BFS

"""

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row, col = len(grid), len(grid[0])
        cnt = 0
        check = [[0]*col for _ in range(row)] # [[0] * col]*row does not work -> it copies the list
        q = deque()

        for i in range(row):
            for j in range(col):
                if (grid[i][j] == "1") and (check[i][j] == 0): # starting point of island
                    q.append((i,j))
                    while q:
                        x, y = q.popleft()
                        check[x][y] = 1
                        print(f"{x} and {y} are visited")
                        for dx, dy in (0,-1), (0,1), (-1,0), (1,0):
                            xx, yy = x+dx, y+dy
                            if (0 <= xx < row) and (0 <= yy < col) and (grid[xx][yy] == '1') and (check[xx][yy] == 0):
                                q.append((xx,yy))
                    cnt += 1

        return cnt
