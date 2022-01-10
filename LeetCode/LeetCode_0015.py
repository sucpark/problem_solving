"""
15. 3Sum (Mediumn)\

Description

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        nums.sort()
        sol = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # avoid duplicate
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue

                temp_sum = nums[i] + nums[left] + nums[right]
                if temp_sum == 0:
                    sol.append([nums[i], nums[left], nums[right]])

                if temp_sum < 0:
                    left += 1
                else:
                    right -= 1
        return sol