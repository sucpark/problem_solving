"""
1614. Maximum Nesting Depth of the Parentheses (Easy)

1. use stack
2. Update the maximum depth
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        deep  = 0
        nest = []
        for c in s:
            if c == '(':
                nest.append(c)
                deep = max(deep, len(nest))
            elif c == ')':
                nest.pop()
        return deep