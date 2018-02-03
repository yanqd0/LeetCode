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
        char2index = SectionCharacterMap()
        for index, ch in enumerate(s):
            previous = char2index[ch]
            if previous < 0:
                current += 1
            else:
                if longest < current:
                    longest = current
                char2index.delete_before(previous)
                current = index - previous
            char2index[ch] = index
        return longest if longest > current else current


class SectionCharacterMap(object):
    def __init__(self):
        self.__map = [-1] * 256
        self.__list = []
        self.__delete_index = -1

    def __setitem__(self, key, value):
        self.__map[ord(key)] = value
        self.__list.append(key)

    def __getitem__(self, item):
        return self.__map[ord(item)]

    def delete_before(self, index):
        for pos in range(self.__delete_index, index):
            key = self.__list[pos + 1]
            self.__map[ord(key)] = -1
        self.__delete_index = index
