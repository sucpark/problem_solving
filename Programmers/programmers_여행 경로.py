"""
여행 경로

1) use dfs
2) if the top element in stack cannot find a ticket, move it to the answer list
"""


def solution(tickets):
    answer = []
    routes = {}
    n_ticket = len(tickets)
    used_ticket = 0

    for d, a in tickets:
        if d in routes:
            routes[d].append(a)
        else:
            routes[d] = [a]

    for k in routes.keys():
        routes[k] = sorted(routes[k], reverse=True)

    stack = ['ICN']
    while stack:
        top = stack[-1]
        if top in routes and routes[top]:
            stack.append(routes[top].pop())
        else:
            answer.append(stack.pop())

    return answer[::-1]