# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n):
        
        a = b = 0

        # if n == 0:
        #     return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        #   n   1   2   3   4   5
        #       1   2   3   5   8

        for i in range(n):
            a, b = b, a + b

            if i == 1:
                a = 1
                b = 1


            # a   b   n
            # 0   0   1
            # 1   1   2
            
            # 3   2   5


        
        return a + b

def test_solution():

    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5
    assert Solution().climbStairs(5) == 8
