"""
조이스틱 (Greedy)

1) use ascii code to compute the upward/downward change count
2) Set the direction to move left or right at the every location
"""


def solution(name):
    answer = 0
    char_change = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]
    curr = 0

    while True:
        answer += char_change[curr]
        char_change[curr] = 0

        if sum(char_change) == 0:
            break

        # Determine the direction which has the shortest length to get the changable character
        left, right = 1, 1
        while char_change[curr - left] == 0:
            left += 1
        while char_change[curr + right] == 0:
            right += 1

        if left < right:
            answer += left
            curr -= left
        else:
            answer += right
            curr += right
    return answer