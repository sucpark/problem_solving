"""
단어 변환

1) use dfs
2) check the changeable words every time
"""


def changeable(word1, word2):
    word = [True if a == b else False for a, b in zip(word1, word2)]
    return True if sum(word) == (len(word) - 1) else False


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    stack = [begin]
    while stack:
        top = stack[-1]
        changeable_top = [w for w in words if changeable(top, w)]
        if target in changeable_top:
            return len(stack)

        if changeable_top:
            stack.append(changeable_top[0])
            words.remove(changeable_top[0])
        else:
            stack.pop()
    return answer