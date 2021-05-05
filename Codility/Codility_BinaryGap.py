"""
BinaryGap
Find longest sequence of zeros in binary representation of an integer.

"""

def solution(N):
    # write your code in Python 3.6

    max_len = 0
    temp_len = -1

    while N != 0:
        b = N % 2
        N = N // 2

        if b == 1:
            max_len = max(max_len, temp_len)
            temp_len = 0
        elif b == 0 and temp_len >= 0:
            temp_len += 1

    return max_len