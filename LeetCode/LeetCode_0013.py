"""
13. Roman to Integer (easy)

"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_order = {'I': 0, 'V': 1, 'X': 2, 'L': 3, 'C': 4, 'D': 5, 'M': 6}
        sol = roman_dict[s[0]]

        for i in range(1, len(s)):
            if roman_order[s[i - 1]] >= roman_order[s[i]]:
                sol += roman_dict[s[i]]
            else:
                sol -= roman_dict[s[i - 1]]
                sol += roman_dict[s[i]] - roman_dict[s[i - 1]]
        return sol