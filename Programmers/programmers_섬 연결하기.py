"""
섬 연결하기

1) use Kruskal algorithm
2) update top parent node
"""


def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    v = [i for i in range(n)]

    for cost in costs:
        s, e, c = cost[0], cost[1], cost[2]
        if s > e:
            s, e = e, s

        vs, ve = v[s], v[e]
        if vs != ve:
            answer += c
            if ve == e:
                v[e] = vs

            for i in range(len(v)):
                if v[i] == ve:
                    v[i] = vs
    return answer