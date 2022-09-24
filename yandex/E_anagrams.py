# https://contest.yandex.ru/contest/8458/problems/E/

# import sys
 
# j = sys.stdin.readline().strip()
# s = sys.stdin.readline().strip()


class Solution:
    def isAnagrams(self, a: str, b: str) -> bool:

        if len(a) != len(b):
            return False

        for letter in a:
            if not letter in b:
                return False
        return True
        
        
def test_solution():
    assert Solution().isAnagrams("qiu","iuq") == True
    assert Solution().isAnagrams("zprl","zprc") == False

