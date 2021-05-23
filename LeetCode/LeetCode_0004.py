"""
4. Median of Two Sorted Arrays (hard)

1) merge two arrays from the back
2) check value of the median position
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)
        size = m + n
        odd = True if size % 2 != 0 else False

        # check the edge cases
        if m == 0:
            if n % 2 == 0:
                return (nums2[n // 2 - 1] + nums2[n // 2]) / 2
            else:
                return nums2[n // 2]
        if n == 0:
            if m % 2 == 0:
                return (nums1[m // 2 - 1] + nums1[m // 2]) / 2
            else:
                return nums1[m // 2]

        nums = []
        if odd:
            target = size // 2 + 1
            while nums1 and nums2:
                top1 = nums1[-1]
                top2 = nums2[-1]
                if top1 > top2:
                    nums.append(nums1.pop())
                else:
                    nums.append(nums2.pop())
                if len(nums) == target:
                    return nums[-1]
            if nums1:
                nums.extend(nums1[::-1])
            if nums2:
                nums.extend(nums2[::-1])
            return nums[target - 1]
        else:
            target = size // 2
            while nums1 and nums2:
                top1 = nums1[-1]
                top2 = nums2[-1]
                if top1 > top2:
                    nums.append(nums1.pop())
                else:
                    nums.append(nums2.pop())
                if len(nums) == target + 1:
                    return (nums[-1] + nums[-2]) / 2

            if nums1:
                nums.extend(nums1[::-1])
            if nums2:
                nums.extend(nums2[::-1])
            return (nums[target - 1] + nums[target]) / 2
