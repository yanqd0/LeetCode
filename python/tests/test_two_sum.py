from leetcode.two_sum import Solution
from pytest import mark, raises

SOLUTION = Solution()


@mark.parametrize('nums, target, expected', [
    ([3, 2, 4], 6, [1, 2]),
    ([3, 2, 3], 6, [0, 2]),
])
def test_two_sum(nums, target, expected):
    assert expected == SOLUTION.twoSum(nums, target)


def test_two_sum_with_err():
    with raises(RuntimeError):
        SOLUTION.twoSum(nums=[1, 2], target=4)
