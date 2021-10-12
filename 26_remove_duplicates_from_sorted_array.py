# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums) -> int:
        
        for x in nums:
            while nums.count(x) > 1:
                nums.remove(x)
        return len(nums)

def test_solution():
    assert Solution().removeDuplicates(nums = [1,1,2]) == 2
    assert Solution().removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]) == 5
