"""
26. Remove Duplicates from Sorted Array (easy)

1) update position when we find the new number
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        unique_num = nums[0]
        new_position = 0

        for i in range(len(nums)):
            if unique_num != nums[i]:
                nums[new_position + 1] = nums[i]
                unique_num = nums[i]
                new_position += 1
        return new_position + 1

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         cnt = len(set(nums))
#         nums[:cnt] = sorted(list(set(nums)))
#
#         return cnt

