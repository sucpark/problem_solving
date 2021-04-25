"""
1773. Count Items Matching a Rule (easy)

1) use hash table
time complexity: O(n)
space complexity: O(1)
"""


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0

        key = {'type': 0, 'color': 1, 'name': 2}

        for item in items:
            if item[key[ruleKey]] == ruleValue:
                cnt += 1
        return cnt