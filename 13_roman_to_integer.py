# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        m4 = s.count('IV')
        m9 = s.count('IX')
        m40 = s.count('XL')
        m90 = s.count('XC')
        m400 = s.count('CD')
        m900 = s.count('CM')
        
        s = s.replace('IV', '')
        s = s.replace('IX', '')
        s = s.replace('XL', '')
        s = s.replace('XC', '')
        s = s.replace('CD', '')
        s = s.replace('CM', '')
        
        a1000 = s.count('M')
        a500 = s.count('D')
        a100 = s.count('C')
        a50 = s.count('L')
        a10 = s.count('X')
        a5 = s.count('V')
        a1 = s.count('I')
        
        n = 0
        
        n = n + a1000 * 1000
        n = n + m900 * 900 # sub
        n = n + a500 * 500
        n = n + m400 * 400 # sub
        n = n + a100 * 100
        n = n + m90 * 90 # sub
        n = n + a50 * 50
        n = n + m40 * 40 # sub
        n = n + a10 * 10
        n = n + m9 * 9 # sub
        n = n + a5 * 5
        n = n + m4 * 4 # sub
        n = n + a1 * 1
        
        
        return n

def test_solution():
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("IV") == 4
    assert Solution().romanToInt("IX") == 9
    assert Solution().romanToInt("LVIII") == 58
    assert Solution().romanToInt("MCMXCIV") == 1994
