"""
1736. Latest Time by Replacing Hidden Digits (easy)

1) split time into hours and minutes
2) check the invalid cases
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        hours = list(time)[:2]
        minutes = list(time)[3:]
        max_digit = {'0': '9', '1': '9', '2': '3'}
        if hours[0] == '?':
            if hours[1] == '?':
                hours[0] = '2'
            elif hours[1] < '4':
                hours[0] = '2'
            else:
                hours[0] = '1'

        if hours[1] == '?':
            hours[1] = max_digit[hours[0]]

        if minutes[0] == '?':
            minutes[0] = '5'
        if minutes[1] == '?':
            minutes[1] = '9'

        sol = hours + [':'] + minutes
        return ''.join(sol)