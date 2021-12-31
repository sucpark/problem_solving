"""
168. Excel Sheet Column Title (Easy)

"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet_dict = {i: c for i, c in enumerate(alphabet)}

        if columnNumber <= 26:
            return alphabet_dict[columnNumber - 1]
        else:
            sol = ''
            while columnNumber > 0:
                remainder = (columnNumber - 1) % 26
                sol += alphabet_dict[remainder]
                columnNumber = (columnNumber - 1) // 26
            return sol[::-1]