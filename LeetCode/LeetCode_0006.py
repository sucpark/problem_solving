"""
6. ZigZag Conversion (medium)

1) update the row pointer based on the position
2) when the row pointer at the bottom (row 0), it is going to upside
3) when the row pointer at the top (row numRows), it is goint to downside
"""


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        row, step = 0, 1

        for x in s:
            # print(L)
            L[row] += x
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(L)
