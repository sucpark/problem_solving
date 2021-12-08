"""
561. Array partition 1

1) for any parings, the minimum value must be contained
2) Thus, we need to drop the smaller one
3) use sort

"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        if not nums or len(nums) == 0:
            return 0

        nums = sorted(nums)
        sol = 0
        for i in range(0, len(nums), 2):
            sol += nums[i]

        return sol