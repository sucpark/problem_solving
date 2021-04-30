"""
8. String to Integer (atoi) (medium)

1) use lstrip() to remove left side whitespace
2) use regular expression to get the pattern
3) return the value based on the range

"""

import re

class Solution:
    def myAtoi(self, s: str) -> int:
        sol = re.match('[+-]?[0-9]+', s.lstrip())
        if sol:
            return max(-2**31, min(2**31-1, int(sol.group(0))))
        return 0