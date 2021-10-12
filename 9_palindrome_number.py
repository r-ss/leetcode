# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reverse = s[::-1]
        if s == reverse:
            return True
        return False

def test_solution():
    assert Solution().isPalindrome(121) == True
    assert Solution().isPalindrome(-121) == False
    assert Solution().isPalindrome(10) == False
    assert Solution().isPalindrome(-101) == False
