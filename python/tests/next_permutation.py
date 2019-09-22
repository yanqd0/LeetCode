from pytest import mark

from leetcode.next_permutation import Solution

from . import read_csv


@mark.parametrize('nums, expect', read_csv(__file__, parser=eval))
def test_two_sum(nums, expect):
    Solution().nextPermutation(nums)
    assert nums == expect
