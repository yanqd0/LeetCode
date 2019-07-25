from pytest import mark

from leetcode.container_with_most_water import Solution

from . import read_csv


@mark.parametrize('height, expect', read_csv(__file__, parser=eval))
def test_longest_palindrome(height, expect):
    assert expect == Solution().maxArea(height)
