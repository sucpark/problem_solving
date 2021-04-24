"""
3. Longest Substring Without Repeating Characters (medium)


1) Check visited characters
2) Reuse obvious length between duplicated characters
    'abcdb' => We know the number of unique characters between b's are 2 (c,a)
3) Check starting point
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_length = 0
        start_idx = 0
        char_dict = {}

        for i, c in enumerate(s):
            if c not in char_dict:
                length = i - start_idx + 1
                max_length = max(max_length, length)
            else:
                start_idx = max(start_idx, char_dict[c] + 1)
                length = i - start_idx + 1
                max_length = max(max_length, length)
            char_dict[c] = i
        return max_length