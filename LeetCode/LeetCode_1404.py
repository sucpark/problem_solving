"""
1404. Number of Steps to Reduce a Number in Binary Representation to One (Medium)

1. Check whether s is even or odd
2. If s is even, use binary shift
3. If s is odd, add 1 from the tail to head
4. If the above process makes s to 0, add 1 at the front of the s
"""


class Solution:
    def numSteps(self, s: str) -> int:
        cnt = 0

        while int(s) != 1:
            if s[-1] == '0':
                s = '0' + s[:-1]
                cnt += 1
                # print(s)
            else:
                temp_s = list(s)
                upper = 1
                for i in range(len(temp_s) - 1, 0 - 1, -1):
                    temp = int(temp_s[i]) + upper
                    if temp > 1:
                        temp_s[i] = '0'
                    else:
                        upper = 0
                        temp_s[i] = '1'
                        break
                s = ''.join(temp_s)
                if int(s) == 0:
                    s = '1' + s
                cnt += 1
                print(s)
        return cnt