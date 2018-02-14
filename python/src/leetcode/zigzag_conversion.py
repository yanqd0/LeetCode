# noinspection SpellCheckingInspection
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number
of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or len(s) <= numRows:
            return s

        result = [''] * numRows
        row, step = 0, 1
        for char in s:
            result[row] += char
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(result)
