"""
136. Single Number (Easy)

Description

a solution with a linear time complexity and constant extra spcae.

=> Cannot use sorting algorithm
=> Cannot use a map or a list

use xor : a^a = 0, 0^a = a
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n

        return res