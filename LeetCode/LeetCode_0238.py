"""
238. Product of Array Except Self (Medium)

1) Brute Force => O(n^2)
2) Two-side multiplication => O(n)

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = []
        m = 1
        for n in nums:
            sol.append(m)
            m *= n

        m = 1
        for i in range(len(sol) - 1, 0 - 1, -1):
            sol[i] = sol[i] * m
            m *= nums[i]
        # print(sol)

        # sol = [1] * len(nums)
        # for i,v in enumerate(nums):
        #     temp = sol[i]
        #     sol = [j * v for j in sol]
        #     sol[i] = temp
        return sol