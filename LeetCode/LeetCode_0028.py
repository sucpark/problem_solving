"""
28. Implement strStr() (easy)



"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1