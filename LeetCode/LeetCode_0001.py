"""
Goal:
    두 수를 합해서 타겟과 같은 값을 가지는 두 수의 인덱스를 반환해라.

Condition:  
    한 수를 두번 이상 쓰면 안된다.
    정답 케이스는 오직 하나만 존재한다.
    음수도 들어올 수 있다.

Method:
    1) Brute Force
        앞에서 부터 비교, 타겟 찾으면 break
    2) Target - First element in nums
    3) Dictionary key 를 이용
    


"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         num_dict = {}
#         for i, n in enumerate(nums):
#             num_dict[i] = n
        
#         num_candidates = list(num_dict.items())
#         len_candidates = len(num_candidates)
        
#         temp_sum = 0
#         sol = []
#         for i in range(len_candidates-1):
#             temp_sum = num_candidates[i][1]
#             for j in range(i+1, len_candidates):
#                 if temp_sum + num_candidates[j][1] == target:
#                     sol.append(num_candidates[i][0])
#                     sol.append(num_candidates[j][0])
#                     break
#          return sol

#         nums_map = {}
#         for i, num in enumerate(nums):
#             nums_map[num] = i               # 동일한 num에 대해 뒤에 있는 index가 기록된다.
        
#         for i, num in enumerate(nums):
#             if target-num in nums_map and i != nums_map[target-num]:   # 값이 존재하고, 인덱스가 서로 다를 경우
#                 return nums.index(num), nums_map[target-num]

        for i, num in enumerate(nums):
            complement = target-num
            if complement in nums[i+1:]:
                return i, nums[i+1:].index(complement) + (i+1)