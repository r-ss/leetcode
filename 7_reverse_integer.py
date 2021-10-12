# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        # x = 0
        s = str(x)
        rev = s[::-1]
        if rev.endswith('-'):
            rev = rev[:-1]
            n = int(rev) * -1
        else:
            n = int(rev)
            
        if abs(n) > 0x7FFFFFFF:
            return 0
            
        return(n)

def test_solution():
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(120) == 21
    assert Solution().reverse(0) == 0
