"""
가장 먼 노드

1) use BFS
2) check the visited nodes
"""

from collections import deque


def solution(n, edge):
    edge_dict = {}
    for s, e in edge:
        if s in edge_dict:
            edge_dict[s].append(e)
        else:
            edge_dict[s] = [e]
        if e in edge_dict:
            edge_dict[e].append(s)
        else:
            edge_dict[e] = [s]

    visited = [False for _ in range(n)]
    distance = [0]

    queue = deque([(1,0)])  # (node, distance)
    visited[0] = True
    while queue:
        n, d = queue.popleft()
        for c in edge_dict[n]:
            if visited[c-1] is False:
                queue.append((c, d+1))
                visited[c-1] = True
                distance.append(d+1)
    answer = distance.count(distance[-1])
    return answer
