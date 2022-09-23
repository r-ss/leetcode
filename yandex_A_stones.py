# https://contest.yandex.ru/contest/8458/problems/A/

# import sys
 
# j = sys.stdin.readline().strip()
# s = sys.stdin.readline().strip()

class Solution:
    def isJewel(self, j: str, s: str) -> int:
        count = 0
        for char in s:
            if char in j:
                count += 1
        return count

def test_solution():
    assert Solution().isJewel("ab", "aabbccd") == 4