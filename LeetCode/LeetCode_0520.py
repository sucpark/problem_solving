"""
520. Detect Capital (Easy)

Description

convert alphabet to ascii code to detect upper case
Consider the several edge cases
1) 'g', 'G' both are possible
2) 'Abc', 'ABC' are possible
3) After checking first two elements, we only need to check the boolean difference between ord(prev) and ord(curr)
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        capitals = range(ord('A'), ord('Z') + 1)
        first = True if ord(word[0]) in capitals else False

        if len(word) == 1:
            return True

        prev = True if ord(word[1]) in capitals else False

        if not first and prev:
            return False

        curr = None

        for i in range(2, len(word)):

            curr = True if ord(word[i]) in capitals else False
            if prev == curr:
                prev = curr
            else:
                return False

        return True