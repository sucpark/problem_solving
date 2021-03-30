"""
Greedy Approach

앞에서 부터 하나씩 넣고. 더 큰게 나오면 빼준다.
앞에서 부터 제거. 최대 뺄 수 있는 개수는 k개

엣지 케이스 1) 111119
엣지 케이스 2) 999
"""


def solution(number, k):
    answer = []
    numbers = list(number)

    for i, n in enumerate(numbers):
        if not answer or answer[-1] >= n:
            answer.append(n)
        else:
            while answer and answer[-1] < n and k > 0:
                answer.pop()
                k -= 1
            answer.append(n)
        if k == 0:
            answer.extend(numbers[i+1:])
            break
    if k > 0:
        answer = answer[:-k]

    answer = ''.join(answer)
    return answer


if __name__ == '__main__':
    data = ['1924', 2]
    print(solution(data[0], data[1]))

    data = ['1231234', 3]
    print(solution(data[0], data[1]))

    data = ['4177252841', 4]
    print(solution(data[0], data[1]))

    data = ['111119', 3]
    print(solution(data[0], data[1]))

    data = ['999', 2]
    print(solution(data[0], data[1]))
