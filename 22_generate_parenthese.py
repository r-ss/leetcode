# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/generate-parentheses/

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        open = '('        
        close = ')'
        bin = []

        def add(o, c, aa=""):

            if o == c == n:
                bin.append(aa)
                return

            if o < n:
                add(o + 1, c, aa=aa+"(")

            if o > c:
                add(o, c + 1, aa=aa+")")

            # add(o, c, aa=aa)

        add(0,0)

        return bin

        

def test_solution():
    assert Solution().generateParenthesis(n = 1) == ["()"]
    assert Solution().generateParenthesis(n = 3) == ["((()))","(()())","(())()","()(())","()()()"]
