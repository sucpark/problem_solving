"""
1390. Four Divisors (Medium)

1) We only need to check the divisor from 1 to sqrt(n) for each number because x*x = n
"""


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        sol = 0
        for n in nums:
            temp = set()
            for i in range(1, floor(sqrt(n)) + 1):
                if n % i == 0:
                    temp.add(i)
                    temp.add(n // i)
                if len(temp) > 4:
                    break
            if len(temp) == 4:
                sol += sum(temp)
        return sol