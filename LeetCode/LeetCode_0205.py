"""
205. Isomorphic Strings (easy)

1) Find the different matching case

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        sol = {}
        if len(set(list(s))) != len(set(list(t))):
            return False

        for i in range(len(s)):
            key = s[i]
            value = t[i]

            if key not in sol:
                sol[key] = value
            else:
                if sol[key] != value:
                    return False
        return True
