from pytest import mark

from leetcode.longest_substring_without_repeating_characters import Solution

SOLUTION = Solution()


# noinspection SpellCheckingInspection
@mark.parametrize('test_str, expect', [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
    ('c', 1),
    ('', 0),
    ('au', 2),
    ('aab', 2),
    ('abba', 2)
])
def test_length_of_longest_substring(test_str, expect):
    assert expect == SOLUTION.lengthOfLongestSubstring(test_str)
