"""
231. Power of Two (easy)

1) Check the edge cases
2) Check the remainder by 2

3) Use bitwise operations
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        if (n & n-1) == 0:
            return True
        else:
            return False

#         if n <= 0:
#             return False

#         if n == 1:
#             return True

#         remainder = 0

#         while remainder == 0 and n > 2:

#             remainder = n % 2
#             n = n // 2

#         if remainder == 0:
#             return True
#         else:
#             return False