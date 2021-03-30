"""

Longest Palindromic Subsequence

1. Odd Length, Even Length 경우를 나눠줘야 한다.
2. 각 경우에 대해 center 를 중심으로 길이를 넓혀가며 최장 길이를 갱신해준다.

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) < 2 or s == s[::-1]:
            return s
        max_len = 0
        sol = ''
        for i in range(len(s)):
            # odd length case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                temp_len = r-l+1
                if temp_len > max_len:
                    sol = s[l:r+1]
                    max_len = temp_len
                l -= 1
                r += 1
            
            # even length case
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                temp_len = r-l+1
                if temp_len > max_len:
                    sol = s[l:r+1]
                    max_len = temp_len
                l -= 1
                r += 1
        return sol