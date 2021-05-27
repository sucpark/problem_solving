"""
소수 찾기

1) use prime dictionary to avoid duplicated computation
2) use permutation
3) only check the half of the number to get the prime number
"""

from itertools import permutations

prime_dict = {0: False, 1: False, 2: True}


def check_prime(n):
    if n in prime_dict:
        if prime_dict[n]:
            return True
        else:
            return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            prime_dict[n] = False
            return False
    prime_dict[n] = True
    return True


def solution(numbers):
    answer = []
    numbers = list(numbers)
    for i in range(len(numbers)):
        temp = list(permutations(numbers, i + 1))
        temp = [''.join(list(e)) for e in temp]
        for t in temp:
            if check_prime(int(t)):
                answer.append(int(t))
    return len(set(answer))