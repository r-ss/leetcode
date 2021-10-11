# https://github.com/r-ss/leetcode

class Solution(object):
    def twoSum(self, nums, target: int):
        m = []
        for idx, item in enumerate(nums):
            for idx2, item2 in enumerate(nums):
                if item + item2 == target:
                    if idx != idx2:
                        m = [idx, idx2]
        return m


def test_solution():
    assert sorted( Solution().twoSum(nums = [2,7,11,15], target = 9)) == [0,1]
    assert sorted( Solution().twoSum(nums = [3,2,4], target = 6)) == [1,2]
    assert sorted( Solution().twoSum(nums = [3,3], target = 6)) == [0,1]