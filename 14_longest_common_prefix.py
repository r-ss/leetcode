# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        
        largestword = strs[0]
        commonprefix = ''
        for s in strs:
            if len(s) > len(largestword):
                largestword = s
                
        for index, char in enumerate(list(largestword)):
            candidate = largestword[:index + 1]
            # print(candidate)
            
            if all(s.startswith(candidate) for s in strs):
                commonprefix = candidate
            # else:
                # commonprefix = ''
            
                        
        return(commonprefix)

def test_solution():
    assert Solution().longestCommonPrefix(strs = ["flower","flow","flight"]) == "fl"
    assert Solution().longestCommonPrefix(strs = ["dog","racecar","car"]) == ""