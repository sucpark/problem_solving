"""
1. alphabet index dict

"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        alpha = list('abcdefghijklmnopqrstuvwxyz'.upper())
        alpha_dict = {c: i + 1 for i, c in enumerate(alpha)}

        sol = 0
        for i, c in enumerate(columnTitle[::-1]):
            sol += (26 ** i) * (alpha_dict[c])
        return sol