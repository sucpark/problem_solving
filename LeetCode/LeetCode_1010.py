"""
1010. Pairs of Songs With Total Durations Divisible by 60 (Medium)

1) use hash map to save the remainder of time
"""


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        temp = [0] * 60
        for t in time:
            remainder = t % 60
            temp[remainder] += 1

        sol = 0
        for i in range(len(temp) // 2 + 1):
            if (i == 0) or (i == 30):
                sol += (temp[i] * (temp[i] - 1)) // 2
            else:
                sol += (temp[i] * temp[60 - i])

        return sol
