"""
2129. Capitalize the Title (Easy)

"""


class Solution:
    def capitalizeTitle(self, title: str) -> str:

        res = []
        words = title.split(' ')
        for word in words:
            if len(word) <= 2:
                res.append(word.lower())
            else:
                res.append(word[0].upper() + word[1:].lower())

        return ' '.join(res)