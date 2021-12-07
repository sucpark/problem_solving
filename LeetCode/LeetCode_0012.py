"""
12. Integer to Roman (medium)

1. Check from the largest value of roman to small
"""


class Solution:
    def intToRoman(self, num: int) -> str:

        value2roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 900: 'CM', 400: 'CD', 90: 'XC',
                       40: 'XL', 9: 'IX', 4: 'IV'}
        values = sorted(list(value2roman.keys()), reverse=True)
        sol = ''

        for v in values:
            while num >= v:
                sol += value2roman[v]
                num -= v

        return sol