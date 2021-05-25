"""
네트워크

1) use DFS
2) check the connection between computers
"""


def solution(n, computers):
    answer = 0
    check = [False for _ in range(n)]
    stack = []

    for i in range(n):
        if check[i] is False:
            stack.append(i)
            check[i] = True
            while stack:
                top = stack.pop()
                for j in range(n):
                    if computers[top][j] == 1 and check[j] is False:
                        stack.append(j)
                        check[j] = True
            answer += 1
    return answer
