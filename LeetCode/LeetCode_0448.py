"""
448. Find All Numbers Disappeared in an Array (easy)

1) use set( )

"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sol = set([i for i in range(1, len(nums) + 1)])
        return list(sol - set(nums))
