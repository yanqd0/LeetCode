from pytest import mark

from leetcode.regular_expression_matching import Solution

from . import read_csv


@mark.parametrize('s, p, expect', read_csv(__file__))
def test_find_median_sorted_arrays(s, p, expect):
    expect = eval(expect)
    solution = Solution()
    assert expect == solution.isMatch(s, p)
