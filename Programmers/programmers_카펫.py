"""
카펫

1) height >= 3
2) width >= height
3) # of boundary = brown
"""


def solution(brown, yellow):
    answer = []
    num = brown + yellow
    for i in range(1, num+1):
        if num % i == 0:
            temp_width = i
            temp_height = int(num / i)
            if temp_width >= temp_height >= 3:
                if 2*temp_width + 2*(temp_height-2) == brown:
                    answer = [temp_width, temp_height]
                    break
    return answer
