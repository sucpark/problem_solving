"""
Queue Reconstruction by Height

1. (h, k) : h = 그 사람의 키, k = 앞에 서 있는 사람 중, 자신의 키 이상인 사람들의 수
1. 키를 기준으로 heap 을 만든다. (파이썬 내장 heapq 는 최소 힙 만 지원한다)
2. 큰 키를 먼저 뽑고, 

"""
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        
        result = []
        while heap:
            temp = heapq.heappop(heap)
            result.insert(temp[1], [-temp[0], temp[1]])
        return result