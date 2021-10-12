# https://github.com/r-ss/leetcode
# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:




        row = 1
        rows = []
        zigzag_direction = 1 # down / up

        # for r in range(numRows):
            # rows.append([666,999])

        for c in range(len(s)):

            

            if zigzag_direction == 1:
                if row == numRows:
                    zigzag_direction = -1 # up
            else:
                if row == 1:
                    zigzag_direction = 1 # down

            rows.append([row, s[c]])

            if numRows > 1:
                row += zigzag_direction

        construct = []

        for r in range(numRows):
            for i in rows:
                if i[0] == r + 1:
                    construct.append(i[1])

            # rows[row] = c
            # row += 1

        print(''.join(construct))

        return ''.join(construct)

#       PAYPALISHIRING

#       12321232123212

#       P   A   H   N
#       A P L S I I G
#       Y   I   R

#       PAHNAPLSIIGYIR
        
        
# Solution().convert(s = "AB", numRows = 1)   

def test_solution():
    assert Solution().convert(s = "PAYPALISHIRING", numRows = 3) == "PAHNAPLSIIGYIR"
    assert Solution().convert(s = "PAYPALISHIRING", numRows = 4) == "PINALSIGYAHRPI"
    assert Solution().convert(s = "A", numRows = 1) == "A"
    assert Solution().convert(s = "AB", numRows = 1) == "AB"
