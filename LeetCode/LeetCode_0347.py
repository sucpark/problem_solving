"""
347. Top K Frequent Elements

1. Count and sort
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == k:
            return nums

        num_dict = {}
        for n in nums:
            if n in num_dict:
                num_dict[n] += 1
            else:
                num_dict[n] = 1
        sol = sorted(num_dict.items(), reverse=True, key=lambda x: x[1])
        return [x for x, y in sol[:k]]