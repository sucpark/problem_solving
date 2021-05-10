"""
17. Letter Combinations of a Phone Number (medium)

1) use double iteration in list comprehension
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(digit_dict[digits])

        sol = ['']
        for d in digits:
            sol = [p + q for p in sol for q in digit_dict[d]]

        return sol