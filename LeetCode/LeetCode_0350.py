"""
350. Intersection of Two Arrays II (easy)

1) use hash
2) hash[key] = [num,num,num..]

"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        h = {}
        sol = []
        for n in nums1:
            if n not in h:
                h[n] = [n]
            else:
                h[n].append(n)

        for n in nums2:
            if n in h and len(h[n]) > 0:
                sol.append(h[n].pop())
        return sol