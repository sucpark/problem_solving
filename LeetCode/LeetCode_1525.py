"""
1525. Number of Good Ways to Split a String (medium)

1) Compute the number of unique character for both sides.
2) Check the point l[i] == r[i+1]


"""


class Solution:
    def numSplits(self, s: str) -> int:

        cnt = 0
        left = []
        right = []
        unique = set()

        for c in s:
            unique.add(c)
            left.append(len(unique))

        unique = set()
        for c in s[::-1]:
            unique.add(c)
            right.append(len(unique))
        right = right[::-1]

        for i in range(1, len(s)):
            if left[i - 1] == right[i]:
                cnt += 1
        return cnt