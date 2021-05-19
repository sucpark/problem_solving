"""
전화번호 목록 (hash)

1) use hash function
"""


def solution(phone_book):
    answer = True
    hash_pb = {}
    for p in phone_book:
        if p not in hash_pb:
            hash_pb[p] = 1

    for pb in phone_book:
        temp = ''
        for p in pb:
            temp += p
            if temp in hash_pb and temp != pb:
                return False
    return answer