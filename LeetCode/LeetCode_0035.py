"""
35. Search Insert Position (Easy)

1) two pointers
2) binary search
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            if (nums[left] < target) and (target < nums[right]):
                left += 1
                right -= 1
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[left] > target:
                return left
            elif nums[right] < target:
                return right + 1

        return left

    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1
    #
    #     if nums[left] > target:
    #         return left
    #     elif nums[right] < target:
    #         return right + 1
    #
    #     while left <= right:
    #         mid = (left + right) // 2
    #
    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid] < target:
    #             left = mid + 1
    #         elif nums[mid] > target:
    #             right = mid - 1
    #     return left