"""
20. Valid Parentheses (easy)

1) use stack
2) divide into two types of buckets, left and right
3) Compare using the index of the bucket
"""


class Solution:
    def isValid(self, s: str) -> bool:

        left = {'(': 0, '{': 1, '[': 2}
        right = {')': 0, '}': 1, ']': 2}

        stack = []

        for p in s:
            if p in left:
                stack.append(p)
            elif p in right:
                if not stack:
                    return False
                curr = stack.pop()
                if left[curr] != right[p]:
                    return False
        if stack:
            return False
        else:
            return True