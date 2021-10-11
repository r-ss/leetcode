# https://github.com/r-ss/leetcode

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if s == s[::-1]:
            return s

        longest = ''
        for n in range(len(s)):
            
            if len(s) - n < len(longest):
                break
            
            for m in range(len(s)):
                
                delta = (m+1) - n
                if delta < len(longest):
                    continue
                
                sub = s[n:m+1]
                if sub == sub[::-1]:
                    if len(sub) > len(longest):
                        longest = sub
        return longest



def test_solution():
    assert Solution().longestPalindrome('babad') in ['bab', 'aba']
    assert Solution().longestPalindrome('cbbd') == 'bb'
    assert Solution().longestPalindrome('a') == 'a'
    assert Solution().longestPalindrome('ac') == 'a'