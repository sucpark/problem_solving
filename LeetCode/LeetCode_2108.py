"""
2108. Find First Palindromic String in the Array (Easy)

"""


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        sol = ""
        for word in words:
            if word == word[::-1]:
                sol = word
                break
        return sol
