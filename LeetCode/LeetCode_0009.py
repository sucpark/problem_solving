"""
9. Palindrome Number (easy)

1) convert integer to string: return str(x) == str(x)[::-1]
2) create reverse integer and compare it

"""

from collections import deque


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x == 0:
            return True
        if x < 0:
            return False

        reverse = 0
        original = x
        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x // 10
        return original == reverse