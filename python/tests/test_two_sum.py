from pytest import mark, raises

from leetcode.two_sum import Solution
from tests import read_csv


@mark.parametrize('nums, target, expect', read_csv(__file__))
def test_two_sum(nums, target, expect):
    assert expect == Solution().twoSum(nums, target)


def test_two_sum_with_err():
    with raises(RuntimeError):
        Solution().twoSum(nums=[1, 2], target=4)
