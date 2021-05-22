"""
k번째수


"""


def solution(array, commands):
    answer = []

    for i, j, k in commands:
        temp = array[i - 1:j]
        temp = sorted(temp)
        answer.append(temp[k - 1])
    return answer
