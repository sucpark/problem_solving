"""
가장 큰 수

1) sort the number using the condition x:xxx
"""

def solution(numbers):
    answer = [str(n) for n in numbers]
    answer = sorted(answer, key=lambda x:x*3, reverse=True)
    return str(int(''.join(answer)))