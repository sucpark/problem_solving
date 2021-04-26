"""
219. Contains Duplicate II (easy)

1) use hash table
2) update the minimum index distance only for duplicated character

time complexicy : O(n)

"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        num_dict = {}
        min_diff = sys.maxsize
        for i, n in enumerate(nums):
            if n not in num_dict:
                num_dict[n] = i
            else:
                min_diff = min(min_diff, abs(i - num_dict[n]))
                num_dict[n] = i
                if min_diff <= k:
                    return True
        return False