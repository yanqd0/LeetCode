from pytest import mark

from leetcode.zigzag_conversion import Solution
from . import read_csv


@mark.parametrize('s, rows, expect', read_csv(__file__, parser=str))
def test_longest_palindrome(s, rows, expect):
    rows = int(rows)
    assert expect == Solution().convert(s, rows)
