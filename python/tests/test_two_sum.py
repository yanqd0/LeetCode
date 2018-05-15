from pytest import mark, raises

from leetcode.two_sum import Solution
from . import read_csv


@mark.parametrize('nums, target, expect', read_csv(__file__, parser=eval))
def test_two_sum(nums, target, expect):
    assert expect == Solution().twoSum(nums, target)


def test_two_sum_with_err():
    with raises(RuntimeError):
        Solution().twoSum(nums=[1, 2], target=4)
