"""
Brackets
Determine whether a given string of parentheses (multiple types) is properly nested.

"""


def solution(S):
    # write your code in Python 3.6
    bucket = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for s in S:
        if s in bucket:
            stack.append(s)
        else:
            if not stack:
                return 0
            else:
                if bucket[stack.pop()] != s:
                    return 0
    if stack:
        return 0
    else:
        return 1