"""
2085. Count Common Words With One Occurrence (Easy)

1) use list.count()
2) use collection Counter()
"""


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        sol = 0
        for w in words1:
            if words1.count(w) == 1 and words2.count(w) == 1:
                sol += 1

        return sol