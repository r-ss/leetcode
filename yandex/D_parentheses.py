# https://contest.yandex.ru/contest/8458/problems/D/

# import sys
 
# j = sys.stdin.readline().strip()
# s = sys.stdin.readline().strip()


class Solution:
    def makeParentheses(self, n: int) -> list[str]:

        bin = []

        def add(o, c, aa=""):

            if o == c == n:
                bin.append(aa)
                return

            if o < n:
                add(o + 1, c, aa=aa+"(")

            if o > c:
                add(o, c + 1, aa=aa+")")

        add(0,0)

        return bin
        
def test_solution():
    assert Solution().makeParentheses(2) == ["(())", "()()"]
    assert Solution().makeParentheses(3) == ["((()))","(()())","(())()","()(())","()()()"]

