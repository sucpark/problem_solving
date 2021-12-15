"""
29. Divide Two Integers (Medium)

1) use bit operator
2) have to consider the edge case (-2^31, 2^31-1)
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == 0:
            return 0

        maxsize = 2 ** 31 - 1
        minsize = -2 ** 31

        if abs(divisor) == 1:
            dividend *= divisor
            if dividend > 0:
                return min(dividend, maxsize)
            else:
                return max(dividend, minsize)

        sign = True if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else False
        dividend = abs(dividend)
        divisor = abs(divisor)
        sol, i = 0, 0

        while dividend >= divisor:
            if dividend >= (divisor << i):
                dividend -= (divisor << i)
                sol += (1 << i)
                i += 1
            else:
                i = 0

        if sign:
            return min(sol, maxsize)
        else:
            return max(-sol, minsize)