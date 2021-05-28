"""
디스크 컨트롤러

1) use queue to handle the task
2) During a task, incoming task is sorted by priority (lower duration)
3) Without processing any task, handle the first incoming task
"""

import heapq
from collections import deque


def solution(jobs):
    answer = 0
    size = len(jobs)
    jobs = deque(sorted(jobs))
    arrive, duration = jobs.popleft()
    end = arrive + duration
    answer += duration
    waiting = []

    while jobs or waiting:
        while jobs and jobs[0][0] <= end:
            temp = jobs.popleft()
            temp = temp[::-1]
            waiting.append(temp)

        if waiting:
            heapq.heapify(waiting)
            next_job = heapq.heappop(waiting)
            waiting_time = end - next_job[1]
            required_time = next_job[0]
            answer = answer + waiting_time + required_time
            end = end + required_time
        else:
            next_job = jobs.popleft()
            waiting_time = next_job[0] - end
            required_time = next_job[1]
            answer = answer + waiting_time + required_time
            end = end + waiting_time + required_time

    return answer // size
