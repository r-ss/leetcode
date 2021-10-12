# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/climbing-stairs/

class Solution:

    def __init__(self):
        self.counter = 0
    def climbStairs(self, n):
        # print('climbStairs >>>', n, self.counter)


        if n == 0:
            # print('>>> returning')
            # print(self.counter)
            if self.counter > 2:
                return self.counter - 1
            return self.counter

        if (n % 2) == 0: # n is even
            # print('even')
            self.counter += 3
            return ( self.climbStairs( n - 2 ) )
        else: # n is odd
            # print('odd')
            self.counter += 1
            return ( self.climbStairs( n - 1 ) )

def test_solution():

    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5
    assert Solution().climbStairs(5) == 8
