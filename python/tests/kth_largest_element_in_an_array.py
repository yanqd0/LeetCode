from pytest import mark, raises

from leetcode.kth_largest_element_in_an_array import Solution

from . import read_csv


@mark.parametrize('nums, k, expect', read_csv(__file__, parser=eval))
def test_two_sum(nums, k, expect):
    assert expect == Solution().findKthLargest(nums, k)
