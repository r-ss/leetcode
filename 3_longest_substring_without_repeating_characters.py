# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# from typing import NewType
# Optional = NewType('Optional', object)

# class Solution:
#     def lengthOfLongestSubstring(self, s:str) -> int:
        
#         # s = "pwwkew"
#         # s = "aab"
#         # s = "bbtablud"
        
#         longest = 0
        
#         for n in range(len(s)):
            
#             for m in range(len(s)):
                
#                 if (n+m+1) > longest:
#                     sub = s[n:m+1]
#                     unique = []

#                     for char in list(sub):
#                         if char not in unique:
#                             unique.append(char)

#                     if len(unique) > longest:
#                         check = ''.join(unique)
#                         if check in sub:
#                             # print(unique)
#                             longest+=1
                        
#         # print(unique)
#         return longest

# Time Limit Cannot Resolve
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)

class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
        

def test_solution():

    assert Solution().lengthOfLongestSubstring('abcabcbb') == 3
    assert Solution().lengthOfLongestSubstring('bbbbb') == 1
    assert Solution().lengthOfLongestSubstring('pwwkew') == 3
    assert Solution().lengthOfLongestSubstring('') == 0