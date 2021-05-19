"""
위장

1) use hash
2) equation = (# of clothes1 - 1)*(# of clothes2 -1) ...  - 1 (the case without any cloth)
"""


def solution(clothes):
    answer = 1
    chash = {}
    for c, k in clothes:
        if k in chash:
            chash[k] += 1
        else:
            chash[k] = 1

    for k, v in chash.items():
        answer *= (v + 1)
    answer -= 1

    return answer