"""
412. Fizz Buzz (easy)

1) Do not use mod becuase it is slower than addition (+)

"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        sol = []
        cnt3 = 0
        cnt5 = 0

        for i in range(1, n + 1):
            cnt3 += 1
            cnt5 += 1
            if cnt3 == 3 and cnt5 == 5:
                sol.append('FizzBuzz')
                cnt3 = 0
                cnt5 = 0
            elif cnt3 == 3 and (cnt5 != 5):
                sol.append('Fizz')
                cnt3 = 0
            elif cnt3 != 3 and cnt5 == 5:
                sol.append("Buzz")
                cnt5 = 0
            else:
                sol.append(str(i))

        return sol