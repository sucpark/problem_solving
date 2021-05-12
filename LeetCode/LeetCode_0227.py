"""
227. Basic Calculator II (medium)

1) use stack
"""


class Solution:
    def calculate(self, s: str) -> int:

        sign = '+'
        num = 0
        stack = []

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)  # 숫자가 한자리가 아닐 수 있다.
            if (not c.isdigit() and not c.isspace()) or (i == len(s) - 1):  # operator 가 나오거나 , 문장이 끝나면 stack에 넣기 시작
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    prev = stack.pop()
                    stack.append(prev * num)
                elif sign == '/':
                    prev = stack.pop()
                    if prev < 0 and prev % num != 0:  # 음의 정수이면서, 소수점이 남을 경우
                        stack.append(prev // num + 1)
                    else:
                        stack.append(prev // num)
                sign = c
                num = 0
        return sum(stack)
