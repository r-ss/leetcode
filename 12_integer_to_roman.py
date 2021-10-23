# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, input: int) -> str:

        n = [ 1000,900,  500, 400,  100, 90,   50,  40,   10,  9,    5,   4,    1 ] # 13
        s = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'] # 13

        c = ''
        ost = input

        for i in range(13):

            if input == n[i]:
                # print('match')
                return s[i]

            # print('loop ost is', ost, 'n[i]', n[i], 'c is', c)

            if ost - n[i] >= 0:
                # print('more', n[i])

                # c = c + s[i]
                # ost -= n[i]

                # print('n', n[i], ost // n[i])
                # is_divisible = ost % n[i] == 0
                # if is_divisible:
                for z in range(int(ost // n[i])):
                    # print('is divisible... c is', c, 's[i] is', s[i], 'z is', z)

                    c += s[i]
                    ost -= n[i]

                    if ost == 0:
                        # print('ZERO')
                        return c
        
        # print(c)
        return c

def test_solution():
    assert Solution().intToRoman(3) == "III"
    assert Solution().intToRoman(4) == "IV"
    assert Solution().intToRoman(9) == "IX"
    assert Solution().intToRoman(21) == "XXI"
    assert Solution().intToRoman(58) == "LVIII"
    assert Solution().intToRoman(1994) == "MCMXCIV"

