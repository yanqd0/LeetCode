from pytest import mark

from leetcode.longest_palindromic_substring import Solution

from . import read_csv


@mark.parametrize('input_str, expect', read_csv(__file__))
def test_longest_palindrome(input_str, expect):
    assert expect == Solution().longestPalindrome(input_str)
