"""
구명보트 (Greedy)

1) sort the people's weight
2) move the index of weight based on the sum of weight
"""


def solution(people, limit):
    answer = 0
    people = sorted(people)
    left, right = 0, len(people) - 1

    while left < right:

        weights = people[left] + people[right]
        if weights > limit:
            right -= 1
            answer += 1
        else:
            right -= 1
            left += 1
            answer += 1
    if left == right:
        answer += 1

    return answer