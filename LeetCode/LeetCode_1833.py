"""
1833. Maximum Ice Cream Bars (Medium)

"""


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        if sum(costs) <= coins:
            return len(costs)

        costs.sort(reverse=True)  # O(nlogn) space
        cnt = 0

        while coins >= costs[-1]:
            cnt += 1
            coins -= costs[-1]
            costs.pop()
            if not costs:
                break
        return cnt