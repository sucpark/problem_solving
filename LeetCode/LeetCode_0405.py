"""
405. Convert a Number to Hexadecimal (easy)


"""
class Solution:
    def toHex(self, num: int) -> str:
        hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        hexa_list = ['', '', '', '', '', '', '', '']
        hexa_idx = 0
        if num == 0:
            return str(num)
        if num > 0:
            while num != 0:
                hexa_list[hexa_idx] = hexa[num % 16]
                num = num // 16
                hexa_idx += 1
            sol = hexa_list[:hexa_idx]
            return ''.join(sol[::-1])
        if num < 0:
            num = -1 * num
            while num != 0:
                hexa_list[hexa_idx] = num % 16
                num = num // 16
                hexa_idx += 1
            if hexa_idx != 8:
                hexa_list[hexa_idx:] = [0] * (8 - hexa_idx)

            print(hexa_list)
            for i in range(len(hexa_list)):
                hexa_list[i] = 15 - hexa_list[i]
            print(hexa_list)
            complement = 1
            for i in range(len(hexa_list)):
                temp = hexa_list[i] + complement
                if temp > 15:
                    hexa_list[i] = hexa[0]
                    complement = 1
                else:
                    hexa_list[i] = hexa[temp]
                    complement = 0

            print(hexa_list)
            return ''.join(hexa_list[::-1])