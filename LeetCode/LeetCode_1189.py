"""
1189. Maximum Number of Balloons (easy)

1) use hash
2) check the minimum cnt of elements of balloon
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        target = set(list('balloon'))
        ball_dict = {c: 0 for c in target}

        for t in text:
            if t in ball_dict:
                ball_dict[t] += 1
        cnt = sys.maxsize

        for c, n in ball_dict.items():
            if c in ['a', 'b', 'n']:
                cnt = min(cnt, n)
            elif c in ['l', 'o']:
                cnt = min(cnt, n // 2)
        return cnt