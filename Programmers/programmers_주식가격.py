"""
주식가격

1) Add -1 at the end of the price (make an end point)
2) Use index of price to calculate the time distance
"""

from collections import deque


def solution(prices):
    if len(prices) == 1:
        return [0]

    answer = [0 for _ in range(len(prices))]
    prices.append(-1)
    prices_idx = deque([(i, p) for i, p in enumerate(prices)])
    stack = []

    while prices_idx:

        if not stack:
            stack.append(prices_idx.popleft())
        else:
            curr = prices_idx[0]
            top = stack[-1]
            if top[1] <= curr[1]:
                stack.append(prices_idx.popleft())
            else:
                if curr[1] != -1:
                    answer[top[0]] = curr[0] - top[0]
                else:
                    answer[top[0]] = curr[0] - top[0] - 1
                stack.pop()
    return answer