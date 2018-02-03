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
"""


# noinspection PyPep8Naming,PyMethodMayBeStatic


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = current = 0
        deleted_index = -1
        char2index = {}
        for index, ch in enumerate(s):
            previous = char2index.get(ch, -1)
            if previous < 0:
                current += 1
            else:
                if longest < current:
                    longest = current
                current = index - previous

                for pos in range(deleted_index, previous):
                    char2index[s[pos + 1]] = -1
                deleted_index = previous
            char2index[ch] = index
        return longest if longest > current else current
