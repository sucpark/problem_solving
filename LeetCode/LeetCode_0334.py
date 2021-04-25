"""
334. Increasing Triplet Subsequence (medium)

1) Compare num with every triple position
2) Update triplet with the smaller one

"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = sys.maxsize

        if len(nums) < 3:
            return False

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False