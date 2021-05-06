"""
746. Min Cost Climbing Stairs (easy)

1) can set the starting point, index 0 or index 1
2) climb one or two steps
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step_cost = [0 for _ in range(len(cost))]
        step_cost[0] = cost[0]
        step_cost[1] = cost[1]
        for i in range(2, len(cost)):
            step_cost[i] = min(step_cost[i - 1], step_cost[i - 2]) + cost[i]

        return min(step_cost[-1], step_cost[-2])