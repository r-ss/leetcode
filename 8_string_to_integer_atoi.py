# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s):
        maxii = 2147483647
        minii = -2147483648
        s = s.strip()
        if not s:
            return 0
        sign, idx = 1, 0
        if s[idx]=='+':
            idx+=1
        elif s[idx]=='-':
            sign = -1
            idx+=1

        num = 0

        n = len(s)
        while idx<n:
            if not s[idx].isdigit():
                break

            num = (num*10)+int(s[idx])

            if num>maxii:
                break
            idx+=1
        return min(max(sign*num, minii), maxii)

def test_solution():
    assert Solution().myAtoi("") == 0
    assert Solution().myAtoi("42") == 42
    assert Solution().myAtoi("   -42") == -42
    assert Solution().myAtoi("4193 with words") == 4193
    assert Solution().myAtoi("words and 987") == 0
    assert Solution().myAtoi("-91283472332") == -2147483648
    assert Solution().myAtoi("3.14159") == 3
    assert Solution().myAtoi("-+12") == 0
    assert Solution().myAtoi(".1") == 0
    assert Solution().myAtoi("+-12") == 0
    assert Solution().myAtoi("+1") == 1
    assert Solution().myAtoi("123-") == 123
    assert Solution().myAtoi("-123+") == -123
    assert Solution().myAtoi("  +  413") == 0
    assert Solution().myAtoi("++1") == 0
    assert Solution().myAtoi("--2") == 0
    assert Solution().myAtoi("  +b12102370352") == 0
    

