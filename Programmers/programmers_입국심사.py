"""
입국심사

1) use binary search
2) check the possible number on the time and reset the time
3) check the minimum time
"""


def solution(n, times):
    left, right = 1, max(times) * n

    while left < right:
        mid = (left + right) // 2
        cnt = sum([mid // t for t in times])
        if cnt >= n:
            right = mid
        else:
            left = mid + 1
    return left