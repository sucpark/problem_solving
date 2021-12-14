"""
485. Max Consecutive Ones (easy)

"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        cnt, max_cnt = 0, 0
        for n in nums:
            if n == 0:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
            else:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
        return max_cnt