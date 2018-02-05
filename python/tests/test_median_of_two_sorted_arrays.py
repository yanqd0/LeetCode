from pytest import mark

from leetcode.median_of_two_sorted_arrays import Solution


@mark.parametrize('nums, target, expected', [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
])
def test_find_median_sorted_arrays(nums1, nums2, expect):
    solution = Solution()
    assert expect == solution.findMedianSortedArrays(nums1, nums2)
