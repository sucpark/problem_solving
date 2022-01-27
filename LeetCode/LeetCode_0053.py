"""
53. Maximum Subarray (Easy)

Description

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # sol, summ = -sys.maxsize, 0
        #
        # for n in nums:
        #     if summ > 0:
        #         summ += n
        #     else:
        #         summ = n
        #
        #     if sol < summ:
        #         sol = summ
        #
        # return sol

        currSum = maxSum = nums[0]

        for i in range(1, len(nums)):

            currSum = max(nums[i], currSum+nums[i])
            maxSum = max(currSum, maxSum)

        return maxSum