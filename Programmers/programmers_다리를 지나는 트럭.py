"""
다리를 지나는 트럭

1) use queue
2) check trucks on the load.
3) update time per each truck

"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    total_weight = 0
    truck_weights = deque(truck_weights)

    end = []
    ing = deque([])

    while ing or truck_weights:
        answer += 1
        if ing:
            ing = deque([(t + 1, w) for t, w in ing])
            if ing[0][0] > bridge_length:
                total_weight -= ing[0][1]
                end.append(ing.popleft())

        if truck_weights and total_weight + truck_weights[0] <= weight:
            total_weight += truck_weights[0]
            ing.append((1, truck_weights.popleft()))

    return answer