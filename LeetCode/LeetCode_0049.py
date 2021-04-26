"""

Group Anagrams

1. string 을 알파벳 단위로 쪼개고, 이를 정렬한 다음 하나의 문자로 만들어준다.
2. 모든 anagrams는 같은 문자를 만드므로, 해당 문자를 key로 받는 dictionary 를 만들어 준다.

python - tim sort를 메인으로 쓰기 때문에 정렬이 매우 빠르다. 

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        str_dic = {}
        for s in strs:
            temp = list(s)
            temp.sort()
            temp = ''.join(temp)
            if temp not in str_dic:
                str_dic[temp] = [s]
            else:
                str_dic[temp].append(s)
        sol = [v for k,v in str_dic.items()]
    
        return sol
    
from collections import defaultdict
class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        str_dic = defaultdict(list)
        for s in strs:
            str_dic[''.join(sorted(s))].append(s)
    
        return str_dic.values()