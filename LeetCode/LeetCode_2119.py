"""
2119. A Number After a Double Reversal (Easy)

"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

        if num < 10:
            return True

        if num % 10 == 0:
            return False

        return True