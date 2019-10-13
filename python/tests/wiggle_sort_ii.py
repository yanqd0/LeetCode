from pytest import mark

from leetcode.wiggle_sort_ii import Solution

from . import read_csv


@mark.timeout(2)
@mark.parametrize('nums', read_csv(__file__, parser=eval))
def test_wiggle_sort(nums):
    Solution().wiggleSort(nums)
    for i, num in enumerate(nums):
        if i % 2 == 0:
            if i == 0:
                continue
            if nums[i - 1] <= num:
                print(i, num, nums[i - 1])
            assert nums[i - 1] > num
        else:
            if nums[i - 1] >= num:
                print(i, num, nums[i - 1])
            assert nums[i - 1] < num


@mark.parametrize(
    'nums, expect', (
        ([1], 1),
        ([1, 2], 1),
        ([1, 2, 1], 1),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 2),
        ([1, 2, 3, 4, 5], 3),
        ([1, 1, 2, 2, 2, 1], 1),
        ([1, 1, 1, 1, 2, 2, 2], 1),
        ([1, 1, 1, 2, 2, 2, 2], 2),
    )
)
def test_kth_max_value(nums, expect):
    assert expect == Solution.kth_max_value(
        nums, 0,
        len(nums) - 1,
        len(nums) // 2
    )


@mark.parametrize(
    'i, expect', (
        (0, 0),
        (1, -1),
        (2, 1),
        (3, -2),
        (4, 2),
        (5, -3),
    )
)
def test_median_index(i, expect):
    assert expect == Solution.median_index(i)


@mark.parametrize(
    'i, length, expect', (
        (0, 4, 1),
        (1, 4, 3),
        (2, 4, 0),
        (3, 4, 2),
        (0, 5, 1),
        (1, 5, 3),
        (2, 5, 0),
        (3, 5, 2),
        (4, 5, 4),
    )
)
def test_map_index(i, length, expect):
    assert expect == Solution.map_index(i, length)


@mark.parametrize(
    'nums, median', (
        ([1], 1),
        ([1, 2], 2),
        ([1, 1, 2], 1),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 2),
        ([1, 2, 3, 4, 5], 3),
        ([1, 3, 3, 4, 5], 3),
        ([1, 3, 3, 4, 3], 3),
        ([1, 3, 3, 3, 3], 3),
        ([1, 1, 1, 1, 2, 2, 2], 1),
        ([3, 3, 3, 2, 2, 2, 3, 2, 1, 1, 2, 1, 2, 3, 3, 3, 1, 2], 2),
    )
)
def test_place_same_median(nums, median):
    Solution.place_same_median(nums, median)

    length = len(nums)
    mid = length // 2
    for i in range(nums.count(median)):
        mid_i = mid + Solution.median_index(i)
        map_i = Solution.map_index(mid_i, length)
        assert nums[map_i] == median
