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
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = end = 0
        str_len = len(s)

        # odd palindrome
        index = (str_len - 1) // 2
        for step in range(str_len):
            index += step if step % 2 else -step
            padding = min(index, str_len - 1 - index)
            if 2 * padding < end - start:
                break

            for half in range(padding + 1):
                if s[index - half] != s[index + half]:
                    half -= 1
                    if end - start < 2 * half or (
                            end - start == 2 * half and
                            index - half < start
                    ):
                        start, end = index - half, index + half
                    break
            else:
                start, end = index - padding, index + padding

        # even palindrome
        index = (str_len - 1) // 2
        for step in range(str_len):
            index -= step if step % 2 else -step
            padding = min(index, str_len - 1 - (index + 1))
            if 2 * padding + 1 < end - start:
                break

            for half in range(padding + 1):
                if s[index - half] != s[index + 1 + half]:
                    half -= 1
                    if end - start < 2 * half + 1 or (
                            end - start == 2 * half + 1 and
                            index - half < start
                    ):
                        start, end = index - half, index + 1 + half
                    break
            else:
                start, end = index - padding, index + 1 + padding

        return s[start: end + 1]
