"""
1446. Consecutive Characters (easy)

"""


class Solution:
    def maxPower(self, s: str) -> int:

        temp = []
        max_len = 0
        for c in s:
            if not temp:
                temp.append(c)
                max_len = max(max_len, len(temp))
            elif c in temp:
                temp.append(c)
                max_len = max(max_len, len(temp))
            else:
                temp = [c]
        return max_len


# class Solution:
#     def maxPower(self, s: str) -> int:
#
#         max_len = 0
#         curr_len = 1
#         prev = s[0]
#
#         for c in s[1:]:
#             if c == prev:
#                 curr_len += 1
#             else:
#                 prev = c
#                 max_len = max(max_len, curr_len)
#                 curr_len = 1
#
#         max_len = max(max_len, curr_len)
#         return max_len