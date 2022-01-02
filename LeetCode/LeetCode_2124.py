"""
2124. Check if All A's Appears Before All B's (Easy)


"""


class Solution:
    def checkString(self, s: str) -> bool:
        b_idx = sys.maxsize

        for i, c in enumerate(s):
            if c == 'a':
                if i > b_idx:
                    return False
            elif c == 'b':
                b_idx = i

        return True
