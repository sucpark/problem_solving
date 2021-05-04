"""
200. Number of Islands (medium)

1) use dfs
2) when I use bfs (use deque() and q.popleft()), time limit exceed

"""


# from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r,c = len(grid), len(grid[0])
        q = [] # deque()
        sol = 0

        visited = [[0]*c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    q.append((i,j))
                    while q:
                        x, y = q.pop()  # q.popleft()
                        visited[x][y] = 1

                        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                            nx, ny = x+dx, y+dy

                            if (0 <= nx < r) and (0 <= ny < c) and (grid[nx][ny] == '1') and (visited[nx][ny] == 0):
                                q.append((nx, ny))
                    sol += 1
        return sol

