"""
70. Climbing Stairs (easy)

1) Dynamic programming (global optimal is the combination of suboptimal)
2) reuse the previous work (memorization)
3) Fibonacci
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        steps = [0 for _ in range(n)]
        steps[0] = 1
        steps[1] = 2

        for i in range(2, n):
            steps[i] = (steps[i - 1]) + (steps[i - 2])

        return steps[n - 1]

#     @cache
#     def climbStairs(self, n: int) -> int:

#         if n == 1:
#             return 1
#         if n == 2:
#             return 2

#         return self.climbStairs(n-1) + self.climbStairs(n-2)