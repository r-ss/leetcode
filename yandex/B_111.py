# https://contest.yandex.ru/contest/8458/problems/B/

# import sys
 
# j = sys.stdin.readline().strip()
# s = sys.stdin.readline().strip()

class Solution:
    def countPrimeros(self, s: str) -> int:

        result = 0
        max = 0
        for i in range(len(s)):
            if s[i] == "1":
                result += 1
            else:
                if max < result:
                    max = result
                result = 0

        return max if max > result else result


def test_solution():
    assert Solution().countPrimeros("510101") == 1
    assert Solution().countPrimeros("51110101") == 3