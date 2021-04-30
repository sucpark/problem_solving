"""
215. Kth Largest Element in an Array (medium)

1) use sort
2) use heapq
"""

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
        # return sorted(nums, reverse=True)[k-1]