"""
단속카메라

1) update camera position based on the exit position
"""


def solution(routes):
    #     answer = 0
    #     routes = sorted(routes, key=lambda x:x[1])
    #     camera = -30001

    #     for route in routes:
    #         if route[0] > camera:
    #             answer += 1
    #             camera = route[1]
    #     return answer

    answer = 1
    routes = sorted(routes, key=lambda x: x[0])
    camera = routes[0][1]
    for route in routes[1:]:
        if route[1] < camera:
            camera = route[1]
        if route[0] > camera:
            answer += 1
            camera = route[1]
    return answer