"""
1200. Minimum Absolute Difference (Easy)

"""


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()  # O(nlogn) time
        sol = []
        min_diff = sys.maxsize

        for i in range(1, len(arr)):  # O(n) time
            curr_diff = abs(arr[i] - arr[i - 1])
            if curr_diff < min_diff:
                min_diff = curr_diff
                sol = [[arr[i - 1], arr[i]]]  # O(n) space
            elif curr_diff == min_diff:
                sol.append([arr[i - 1], arr[i]])
        return sol