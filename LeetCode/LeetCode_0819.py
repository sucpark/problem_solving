"""

1. Delete punctuation
2. Count words
3. Find the frequent word

"""

import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        word_cnt = {}
        paragraph = re.sub(r'[^A-Za-z0-9]+', ' ', paragraph).lower().split() # Replace punctuations with ' ' instead of ''
        for word in paragraph:
            if word not in banned:
                if word not in word_cnt:
                    word_cnt[word] = 1
                else:
                    word_cnt[word] += 1
        max_word = max(word_cnt, key=lambda x: word_cnt[x])
        print(word_cnt)
        return max_word