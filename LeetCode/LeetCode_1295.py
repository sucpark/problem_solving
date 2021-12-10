"""
1295. Find Numbers with Even Number of Digits (easy)

1) convert number to string
2) check the digit unit log or //10
"""


class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        cnt = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                cnt += 1
        return cnt