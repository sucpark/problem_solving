"""
2094. Finding 3-Digit Even Numbers (easy)

1) use permutation function (brute force)
2) check every three-digit number's components (O(n))
"""


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        sol = set()
        for x, y, z in permutations(digits, 3):
            if x != 0 and z % 2 == 0:
                sol.add(100 * x + 10 * y + z)
        return sorted(list(sol))


# class Solution:
#     def findEvenNumbers(self, digits: List[int]) -> List[int]:
#         ans = []
#         freq = Counter(digits)
#         for x in range(100, 1000, 2):
#             print(int(d) for d in str(x))
#             if not Counter(int(d) for d in str(x)) - freq:
#                 ans.append(x)
#         return ans