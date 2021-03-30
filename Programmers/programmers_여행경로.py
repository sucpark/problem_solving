"""
2021.02.26

Used DFS to solve the problem

"""


def solution(tickets):

    # Store the routes as dictionary
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]

    for r in routes:
        routes[r].sort(reverse=True)

    stack = ['ICN']
    path = []

    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:  # End case
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())

    return path[::-1]


if __name__ == '__main__':
    data1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    data2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    data3 = [["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]

    sol1 = solution(data1)
    sol2 = solution(data2)
    sol3 = solution(data3)

    print(sol1)
    print(sol2)
    print(sol3)
