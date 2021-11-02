# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str):

        #  2      3      4      5      6      7       8      9
        # ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # print(len(digits))

        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return list(kvmaps[digits[0]])

        variations = []

        for a in kvmaps[digits[0]]:
            variations.append(a) # first letters

        for i in range(1, len(digits)):
            # print(i)

            newvars = []
            for v in variations:
            
                for b in kvmaps[digits[i]]:
                    word = v + b
                    newvars.append(word)

            variations = newvars
        
        return sorted(variations)

def test_solution():
    assert Solution().letterCombinations(digits = "23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert Solution().letterCombinations("") == []
    assert Solution().letterCombinations("2") == ["a","b","c"]
    assert Solution().letterCombinations("22") == ["aa","ab","ac","ba","bb","bc","ca","cb","cc"]
    assert Solution().letterCombinations("234") == ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
    