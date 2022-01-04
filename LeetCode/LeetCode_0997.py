"""
997. Find the Town Judge (Easy)

1) get the judge candidate : judge trusts nobody
2) check the candidate is trusted by the others
"""


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        people = set()
        judge = [0] * (n + 1)
        for a, b in trust:
            people.add(a)
            judge[b] += 1

        judge_candidate = set(range(1, n + 1)) - people     # only get one people
        if judge_candidate:
            sol = judge_candidate.pop()
            if judge[sol] == n - 1:
                return sol
        return -1