"""
316. Remove Duplicated Letters

1) the smallest
2) lexicographical order
3) unique characters

"""
from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:

        stack = []
        count = Counter(s)

        for c in s:
            count[c] -= 1

            if c in stack:
                continue
            while stack and c < stack[-1] and count[stack[-1]] > 0:
                stack.pop()
            stack.append(c)
        return ''.join(stack)