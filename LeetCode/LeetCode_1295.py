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


# def CheckEvenDigit(num: int) -> bool:
#     cnt = 0
#     while num > 0:
#         num //= 10
#         cnt += 1
#
#     if cnt % 2 == 0:
#         return True
#     else:
#         return False
#
#
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#
#         cnt = 0
#         for x in nums:
#             if CheckEvenDigit(x):
#                 cnt += 1
#
#         return cnt
