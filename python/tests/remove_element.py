from pytest import mark

from leetcode.remove_element import Solution

from . import read_csv


@mark.parametrize(
    'nums, val, expect, new_nums',
    read_csv(__file__, parser=eval),
)
def test_two_sum(nums, val, expect, new_nums):
    assert expect == Solution().removeElement(nums, val)
    assert nums == new_nums
