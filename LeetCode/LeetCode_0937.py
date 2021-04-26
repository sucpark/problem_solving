"""

1. 문자와 숫자를 구분한다.
2. 문자를 정렬한다.

"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log = []
        digit_log = []
        
        for log in logs:
            temp = log.split()
            if temp[1].isnumeric():     # Check whether 
                digit_log.append(log)
            else:
                letter_log.append(log)
        letter_log.sort(key = lambda x: (x.split()[1:], x.split()[0])) # Sort by two conditions

        return letter_log + digit_log
        
   