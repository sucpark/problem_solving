"""
모의고사

1) create the student's answers
2) compute the student's score
3) create dictionary with key as score, value as student idx
"""


def solution(answers):
    if len(answers) == 0:
        return []

    answer = []
    correct = [0] * 3
    size = len(answers)
    s1 = [1, 2, 3, 4, 5]
    s1 = s1 * (size // len(s1)) + s1[:size % len(s1)]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s2 = s2 * (size // len(s2)) + s2[:size % len(s2)]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s3 = s3 * (size // len(s3)) + s3[:size % len(s3)]

    for i, a in enumerate(answers):
        if s1[i] == a:
            correct[0] += 1
        if s2[i] == a:
            correct[1] += 1
        if s3[i] == a:
            correct[2] += 1

    max_score = max(correct)
    for i, c in enumerate(correct):
        if c == max_score:
            answer.append(i + 1)
    return answer
