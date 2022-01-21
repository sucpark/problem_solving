"""
2138. Divide a String Into Groups of Size k (Easy)

"""


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        res = []

        while len(s) >= k:
            res.append(s[:k])
            s = s[k:]

        if len(s) > 0:
            while len(s) != k:
                s += fill

            res.append(s)

        return res