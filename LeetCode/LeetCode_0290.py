"""
290. Word Pattern (easy)

1) Check the case with different key-value pair
2) Check the invalid case
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        sol1 = {}
        sol2 = {}

        for i in range(len(pattern)):
            if pattern[i] not in sol1:
                sol1[pattern[i]] = words[i]
            else:
                if sol1[pattern[i]] != words[i]:
                    return False

            if words[i] not in sol2:
                sol2[words[i]] = pattern[i]
            else:
                if sol2[words[i]] != pattern[i]:
                    return False
        return True