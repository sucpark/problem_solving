"""
H-Index

1) sort the citations
2) case: [6,6,6,5,2] -> 4 : the point that a citation becomes smaller than index is the solution
3) case: [44, 22] -> 2 : for loop cannot catch the case
"""


def solution(citations):
    if len(citations) == 1:
        return 1 if citations[0] == 1 else 0

    citations = sorted(citations, reverse=True)
    for i, c in enumerate(citations):
        if i + 1 > c:
            return i
    return len(citations)