# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums, val):
        
        while val in nums:
            nums.remove(val)
        
        return len(nums)
        

def test_solution():
    assert Solution().removeElement(nums = [3,2,2,3], val = 3) == 2
    assert Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2) == 5
