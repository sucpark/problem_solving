"""
이중우선순위 큐

1) use heapq to find min value
2) to delete max value, find the index and pop it
"""

import heapq


def solution(operations):
    answer = []
    heapq.heapify(answer)

    for o in operations:
        if o.startswith('I'):
            heapq.heappush(answer, int(o.split()[1]))
        elif o == 'D 1':
            if answer:
                max_element = max(answer)
                max_idx = answer.index(max_element)
                answer.pop(max_idx)
            else:
                continue
        elif o == 'D -1':
            if answer:
                heapq.heappop(answer)
            else:
                continue
    if answer:
        return [max(answer), answer[0]]
    else:
        return [0, 0]