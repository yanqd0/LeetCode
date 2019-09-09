from pytest import mark

from leetcode.merge_intervals import Solution

from . import read_csv


@mark.parametrize('intervals, expect', read_csv(__file__, parser=eval))
def test_two_sum(intervals, expect):
    assert expect == Solution().merge(intervals)
