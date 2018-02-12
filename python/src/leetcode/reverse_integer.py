"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within
the 32-bit signed integer range. For the purpose of this problem, assume that
your function returns 0 when the reversed integer overflows.

https://leetcode.com/problems/reverse-integer/
"""

MAX_INT = 2 ** 31 - 1
MIN_INT = -2 ** 31


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > MAX_INT or x < MIN_INT:
            return 0

        s, sign = (str(x), 1) if x > 0 else (str(-x), -1)
        rev = sign * int(s[::-1])
        return 0 if rev > MAX_INT or rev < MIN_INT else rev
