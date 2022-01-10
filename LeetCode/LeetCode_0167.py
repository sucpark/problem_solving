"""
167. Two Sum II - Input Array Is Sorted (Easy)

Description
Since the array is sorted, we can use two pointers.
Let's set the two index pointers, 0 and len(array)-1.
If the sum of two pointers is larger than target, move the right pointer to add smaller one.
If the sum of two pointers is less than target, move the left pointer to add bigger one
If the sum is the same with the target, return the indexes + 1.

In addition, like the solution of problem 1. Two Sum, we can use hash function to solve the problem.
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]


# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#
#         seen = {}
#         for i, n in enumerate(numbers):
#             remaining = target - n
#             if remaining in seen:
#                 return [seen[remaining] + 1, i + 1]
#             else:
#                 seen[n] = i