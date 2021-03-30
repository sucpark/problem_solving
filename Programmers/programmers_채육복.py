"""
2021.02.27

Greedy approach

빌려주는 순서 중요. 내가 잃어버렸으면 내껄 먼저 챙겨야 한다.
모든 케이스를 다 돌면 안되고, 조사 범위를 한정해야 한다.

"""


def solution(n, lost, reserve):  

    answer = n
    real_lost = [x for x in lost if x not in reserve]
    real_reserve = [x for x in reserve if x not in lost]

    for i in real_lost:
        if (i-1) in real_reserve:
            real_reserve.remove(i-1)
        elif (i+1) in real_reserve:
            real_reserve.remove(i+1)
        else:
            answer -= 1

    return answer


if __name__ == '__main__':

    data = [5, [2, 4], [1, 3, 5]]
    print(solution(data[0], data[1], data[2]))

    data = [5, [2, 4], [3]]
    print(solution(data[0], data[1], data[2]))

    data = [3, [3], [1]]
    print(solution(data[0], data[1], data[2]))
