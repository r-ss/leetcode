# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/regular-expression-matching/

import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # if len(p) < len(s):
            # return False
        if p == s:
            return True

        pc = '^('
        for i in range(len(p)):
            c = p[i]
            if c in 'abcdefghijklmnopqrstuvwxyz':
                print('>>>>> a-z')
                if i + 1  < len(p):
                    if p[i + 1] == '*':
                        # print('passing', c, pc, s, p)
                        continue
                pc = pc + '%s{1}' % c
            if c == '.':
                print('>>>>> .')
                # pc = pc + '[a-z]{1}'
                if i + 1  < len(p):
                    if p[i + 1] == '*':
                        continue
                pc = pc + '[a-z]{1}'
            if c == '*':
                print('>>>>> *')
                if p[i - 1] == '.':
                    pc = pc + '[a-z]*'
                else:
                    pc = pc + '%s*' % p[i - 1]

        pc = pc + ')$'

        # p = '%s[%s,%s]' % (p, min, max)


        # pattern = re.compile(pc)

        print('matching', s, 'to', pc, 'result', re.match(pc, s))

        if re.match(pc, s):
            return True
            # print(r1)
        else:
            print('no match?')
        
        return False

def test_solution():
    assert Solution().isMatch(s = "aaa", p = ".*") == True
    assert Solution().isMatch(s = "aaa", p = "ab*a") == False
    assert Solution().isMatch(s = "aaa", p = "a.a") == True
    assert Solution().isMatch(s = "aa", p = "a") == False
    assert Solution().isMatch(s = "aa", p = "a*") == True
    assert Solution().isMatch(s = "ab", p = ".*") == True
    assert Solution().isMatch(s = "aab", p = "c*a*b") == True
    assert Solution().isMatch(s = "mississippi", p = "mis*is*p*.") == False
    assert Solution().isMatch(s = "aa", p = "aa") == True
    assert Solution().isMatch(s = "aaa", p = "ab*ac*a") == True
    
    
