# noinspection SpellCheckingInspection
"""
Given a string, find the length of the longest substring without
repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        last = -1
        char2index = [-1] * 128
        for index, ch in enumerate(s):
            previous = char2index[ord(ch)]
            if previous >= 0:
                longest = max(longest, index - last - 1)
                for pos in range(last, previous):
                    char2index[ord(s[pos + 1])] = -1
                last = previous
            char2index[ord(ch)] = index
        return max(longest, len(s) - last - 1)


# Python 2
# Runtime: 40 ms, faster than 91.84% of Python online submissions
# for Longest Substring Without Repeating Characters.
# Memory Usage: 12.2 MB, less than 43.75% of Python online submissions
# for Longest Substring Without Repeating Characters.
#
# Python 3
# Runtime: 76 ms, faster than 62.44% of Python3 online submissions
# for Longest Substring Without Repeating Characters.
# Memory Usage: 13.2 MB, less than 81.34% of Python3 online submissions
# for Longest Substring Without Repeating Characters.
