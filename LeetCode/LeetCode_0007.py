"""
7. Reverse Integer (easy)

1) use stack
2) check the edge cases

"""


class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:
            return 0

        sign = 1
        if x < 0:
            x = -1 * x
            sign = -1

        stack = []

        while x != 0:
            stack.append(str(x % 10))
            x = x // 10

        if stack[0] == '0':
            stack = stack[1:]

        sol = sign * int(''.join(stack))
        if sol in range(-2 ** 31, 2 ** 31):
            return sol
        else:
            return 0