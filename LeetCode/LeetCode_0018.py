"""
18. 4Sum (Medium)

Description

"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        nums.sort()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left, right = j + 1, len(nums) - 1

                while left < right:
                    temp_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if temp_sum < target:
                        left += 1
                    elif temp_sum > target:
                        right -= 1
                    else:
                        temp_ans = [nums[i], nums[j], nums[left], nums[right]]
                        if temp_ans not in ans:
                            ans.append(temp_ans)
                        left += 1
                        right -= 1
        return ans