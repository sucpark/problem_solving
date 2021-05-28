"""
더 맵게 (heap)

1) use priority queue
2) check the number of remaining scoville index
"""

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) >= 2:
            top1 = heapq.heappop(scoville)
            top2 = heapq.heappop(scoville)
            mix = top1 + top2 * 2
            answer += 1
            heapq.heappush(scoville, mix)
        else:
            return -1

    return answer