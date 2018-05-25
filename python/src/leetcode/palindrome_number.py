"""
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left,
             it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Could you solve it without converting the integer to a string?
"""

from math import log


# noinspection PyPep8Naming
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True

        high = int(log(x, 10))
        low = 0
        while low < high:
            if self.number_of(x, low) == self.number_of(x, high):
                low += 1
                high -= 1
            else:
                return False
        else:
            return True

    @staticmethod
    def number_of(x, base):
        return x % (10 ** (base + 1)) // (10 ** base)
