# https://contest.yandex.ru/contest/8458/problems/C/

# import sys
 
# j = sys.stdin.readline().strip()
# s = sys.stdin.readline().strip()


class Solution:
    def removeDuplicates(self, nums: list[int]) -> list:

        nums = nums[1:]
        filtered = []
    
        for x in nums:
            if x not in filtered:
                filtered.append(x)

        # print(filtered)
        return filtered
        
def test_solution():
    assert Solution().removeDuplicates([5,2,4,8,8,8]) == [2,4,8]
    assert Solution().removeDuplicates([5,2,2,2,8,8]) == [2,8]