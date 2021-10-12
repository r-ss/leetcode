# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # print (len(haystack))

        if needle == '':
            return 0

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
        

def test_solution():
    assert Solution().strStr(haystack = "hello", needle = "ll") == 2
    assert Solution().strStr(haystack = "aaaaa", needle = "bba") == -1
    assert Solution().strStr(haystack = "", needle = "") == 0
