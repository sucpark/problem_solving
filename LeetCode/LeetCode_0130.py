"""
130. Surrounded Regions (medium)


1) Use DFS
2) Check the island contains a border.
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        r, c = len(board), len(board[0])
        visited = [[False for _ in range(c)] for _ in range(r)]
        stack = []
        islands = []
        border = False

        for i in range(r):
            for j in range(c):
                if (board[i][j] == 'O') and (visited[i][j] is False):
                    stack.append((i, j))
                    visited[i][j] = True

                    while stack:
                        x, y = stack.pop()
                        islands.append((x, y))
                        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                            tx, ty = x + dx, y + dy
                            if (0 <= tx < r) and (0 <= ty < c):
                                if (board[tx][ty] == 'O') and (visited[tx][ty] is False):
                                    stack.append((tx, ty))
                                    visited[tx][ty] = True
                            else:
                                border = True
                    if not border:
                        for x, y in islands:  # When I set (x,y) as (i,j), it does not work becuase the redefined i affect the i in the for loop.
                            board[x][y] = 'X'

                    islands = []
                    border = False