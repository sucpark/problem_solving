"""
438. Find All Anagrams in a String (medium)

1) use hash table
2) compare the substring with p based on the hash table
"""

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        length = len(p)
        temp = Counter(p)
        sol = []

        for i in range(len(s) - length + 1):
            temp_s = s[i:i + length]
            if Counter(temp_s) == temp:
                # if set(temp_s) == set(p):
                sol.append(i)
        return sol