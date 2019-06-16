from pytest import mark

from leetcode.reverse_integer import Solution

from . import read_csv


@mark.parametrize('x, expect', read_csv(__file__, parser=int))
def test_longest_palindrome(x, expect):
    assert expect == Solution().reverse(x)
