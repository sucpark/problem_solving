"""
프린터

1) use queue
2) check the maximum priority in the printer queue
"""

from collections import deque
def solution(priorities, location):

    queue = deque(list(zip(range(len(priorities)), priorities)))
    sorted_priorities = sorted(priorities)
    result = []
    while queue:
        l,p = queue.popleft()
        if p < sorted_priorities[-1]:
            queue.append((l,p))
        else:
            result.append(p)
            sorted_priorities.pop()
            if l == location:
                return len(result)    