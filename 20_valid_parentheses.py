# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        
        open_a = 0
        open_b = 0
        open_c = 0
        lastopen = []
        
        # s = "()[]{}"
        # s = "{[]}"
        
        # open = '({['
        
        # close = ')}]'
        if s[0] in ')}]':
            return False
        
        error = False
        
        for index, char in enumerate(s):
            
            if char == '(':
                lastopen.append(char)
                open_a += 1
            if char == '[':
                lastopen.append(char)
                open_b += 1
            if char == '{':
                lastopen.append(char)
                open_c += 1
                
            
                
            if char == ')':
                if lastopen and lastopen[-1] == '(':
                    lastopen = lastopen[:-1]
                    open_a -= 1
                else:
                    error = True
            
            if char == ']':
                if lastopen and lastopen[-1] == '[':
                    lastopen = lastopen[:-1]
                    open_b -= 1
                else:
                    error = True
            
            if char == '}':
                if lastopen and lastopen[-1] == '{':
                    lastopen = lastopen[:-1]
                    open_c -= 1
                else:
                    error = True
                
            # print(lastopen)

        if sum([open_a, open_b, open_c]) != 0:
            error = True
            
            
        print(open_a, open_b, open_c)
        return not error

def test_solution():
    assert Solution().isValid(s = "()") == True
    assert Solution().isValid(s = "()[]{}") == True
    assert Solution().isValid(s = "(]") == False
    assert Solution().isValid(s = "([)]") == False
    assert Solution().isValid(s = "{[]}") == True
