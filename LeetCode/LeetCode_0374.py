"""
374. Guess Number Higher or Lower (easy)

"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        if guess(n) == 0:
            return n

        s, l = 1, n
        sol = (s + l) // 2

        while guess(sol) != 0:
            if guess(sol) > 0:
                s = sol
                sol = (s + l) // 2

            elif guess(sol) < 0:
                l = sol
                sol = (s + l) // 2
        return sol
