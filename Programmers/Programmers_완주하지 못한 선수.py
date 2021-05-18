"""
완주하지 못한 선수

1) use hash function
2) sorting
"""


def solution(participant, completion):
    if len(participant) == 1:
        return participant[0]

    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]