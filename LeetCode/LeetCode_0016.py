"""
16. 3Sum Closest (Medium)

1) use two pointers approach
2) adjust point based on current sum compared to target (sorted num is required)

"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sol = 0
        min_diff = sys.maxsize
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            forward = i + 1
            backward = len(nums) - 1

            while forward < backward:
                curr = nums[i] + nums[forward] + nums[backward]
                if abs(curr - target) < min_diff:
                    min_diff = abs(curr - target)
                    sol = curr
                if curr < target:
                    forward += 1
                elif curr > target:
                    backward -= 1
                else:
                    return sol
        return sol