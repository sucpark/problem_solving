"""
방문길이

1) create 4-dimension array to check the path, not a visited point

"""


def solution(dirs):
    answer = 0
    direction = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    unvisited = [[[[True for _ in range(-5, 6)] for _ in range(-5, 6)] for _ in range(-5, 6)] for _ in range(-5, 6)]

    x, y = 5, 5
    for d in dirs:
        dx, dy = direction[d]
        if (0 <= x + dx <= 10) and (0 <= y + dy <= 10):
            nx, ny = x + dx, y + dy
            if unvisited[x][nx][y][ny]:
                # print(f"({x-5}, {y-5}), ({nx-5}, {ny-5})")
                unvisited[x][nx][y][ny] = False
                unvisited[nx][x][ny][y] = False
                answer += 1
            x, y = nx, ny
    return answer