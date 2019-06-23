# noinspection SpellCheckingInspection
"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.



Example:

Input: "cbbd"

Output: "bb"

https://leetcode.com/problems/longest-palindromic-substring/
"""


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        length = len(s)
        for fix in range(2):
            center = (length - 1) // 2
            for step in range(length):
                center += step if (step + fix) % 2 else -step
                padding = min(center, length - 1 - (center + fix))
                if 2 * padding + fix < end - start:
                    break

                for half in range(padding + 1):
                    if s[center - half] != s[center + fix + half]:
                        half -= 1
                        if end - start < 2 * half + fix or (
                            end - start == 2 * half + fix
                            and center - half < start
                        ):
                            start, end = center - half, center + fix + half
                        break
                else:
                    start, end = center - padding, center + fix + padding
        return s[start:end + 1]


# Python 2
# Runtime: 204 ms, faster than 90.21% of Python online submissions
# for Longest Palindromic Substring.
# Memory Usage: 11.8 MB, less than 57.96% of Python online submissions
# for Longest Palindromic Substring.
#
# Python 3
# Runtime: 132 ms, faster than 90.76% of Python3 online submissions
# for Longest Palindromic Substring.
# Memory Usage: 13.2 MB, less than 63.56% of Python3 online submissions
# for Longest Palindromic Substring.
