"""
1684. Count the Number of Consistent Strings (easy)

1) use set
"""


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        cnt = 0
        for word in words:
            temp = set(word)
            if not temp-allowed:
                cnt += 1
        return cnt