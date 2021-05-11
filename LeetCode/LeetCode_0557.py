"""
557. Reverse Words in a String III (easy)

1) add reversed words and merge it

"""


class Solution:
    def reverseWords(self, s: str) -> str:

        if len(s) == 1:
            return s

        sol = []
        for i in s.split():
            sol.append(i[::-1])

        return ' '.join(sol)