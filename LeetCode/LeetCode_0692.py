"""
692. Top K Frequent Words (medium)


1) Compute count for each word
2) Use hash table, count as key and words as value
    {2: ['i', 'love'], 1: ['leetcode', 'coding']}
3) Add list from the larger key, return when the number of words in sol is larger than k
"""

from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        word_cnt = list(Counter(words).items())

        dict_k = {}
        for wc in word_cnt:

            if wc[1] not in dict_k:
                dict_k[wc[1]] = [wc[0]]
            else:
                dict_k[wc[1]].append(wc[0])
        dict_k = sorted(dict_k.items(), reverse=True)
        sol = []

        for _, word in dict_k:
            sol.extend(sorted(word))
            if len(sol) > k:
                break
        return sol[:k]