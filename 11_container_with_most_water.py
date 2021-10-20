# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height) -> int:
        
        L, R, mx = 0, len(height) - 1, 0

        while R >= L:
            LH = height[L]
            RH = height[R]
            width = R - L
            area = min(LH, RH) * width
            mx = max(mx, area)

            if LH > RH:
                R -= 1
            else:
                L += 1

        return mx


def test_solution():
    assert Solution().maxArea(height = [1,1]) == 1
    assert Solution().maxArea(height = [4,3,2,1,4]) == 16
    assert Solution().maxArea(height = [1,2,1]) == 2
    assert Solution().maxArea(height = [1,8,6,2,5,4,8,3,7]) == 49

