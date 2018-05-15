from pytest import mark

from leetcode.longest_substring_without_repeating_characters import Solution
from . import read_csv


@mark.parametrize('test_str, expect', read_csv(__file__, parser=str))
def test_length_of_longest_substring(test_str, expect):
    expect = int(expect)
    assert expect == Solution().lengthOfLongestSubstring(test_str)
