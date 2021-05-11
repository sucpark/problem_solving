"""
541. Reverse String II (easy)

1) divide the string based on the size of k

"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        if len(s) < k:
            return s[::-1]

        if k <= len(s) < 2 * k:
            return s[:k][::-1] + s[k:]

        gap = 2 * k
        size = len(s)
        remainder = size % gap
        sol = []
        for i in range(0, size - remainder, gap):
            start, end = i, i + k
            sol.append(s[start:end][::-1] + s[end:end + k])

        if size % gap < k:
            sol.append(s[size - remainder:][::-1])
        else:
            sol.append(s[size - remainder:size - remainder + k][::-1] + s[size - remainder + k:])

        return ''.join(sol)