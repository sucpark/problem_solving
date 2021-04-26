"""
217. Contains Duplicate

1. Use hash table
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        d = {}
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = 1
        return False