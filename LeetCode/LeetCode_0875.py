"""
875. Koko Eating Bananas (medium)

Contraint
1. eat all bananas within h hours
2. minimum integer k

Sol
1. binary search
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def get_possible_k(k):
            cnt = 0
            for i in piles:
                cnt += ceil(i / k)

            return cnt <= h

        fastest = max(piles)
        k = 1

        while k < fastest:
            mid = k + (fastest - k) // 2

            if get_possible_k(mid):
                fastest = mid
            else:
                k = mid + 1
        return k