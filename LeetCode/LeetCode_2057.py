"""
2057. Smallest Index With Equal Value (Easy)

"""


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:

        for i, n in enumerate(nums):  # O(n)
            if i % 10 == n:
                return i
        return -1