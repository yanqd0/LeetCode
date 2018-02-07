from pytest import mark

from leetcode.median_of_two_sorted_arrays import Solution


@mark.parametrize('nums1, nums2, expect', [
    ([], [1], 1.0),
    ([2], [], 2.0),
    ([2], [1, 3, 4], 2.5),
    ([1, 2, 4], [3], 2.5),
    ([3], [1, 2], 2.0),
    ([2], [1, 3, 4, 5], 3.0),
    ([4], [1, 2, 3, 5], 3.0),
    ([1, 4], [2, 3, 5, 6, 7], 4.0),
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
    ([1, 3], [2, 4], 2.5),
    ([2, 3], [1, 4], 2.5),
    ([1], [3], 2.0),
    ([1], [1, 2, 3, 4], 2.0),
    ([9], [1, 2, 3, 4], 3.0),
    ([1, 2, 3, 4, 5, 6], [1, 2], 2.5),
    ([1, 2, 3, 4, 5, 6], [3, 4], 3.5),
    ([1, 2, 3, 4, 5, 6], [5, 6], 4.5),
    ([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 8, 9], 5.0),
    ([1, 2, 3, 4, 8, 9], [3, 4, 5, 6, 7, 8, 9], 5.0),
])
def test_find_median_sorted_arrays(nums1, nums2, expect):
    solution = Solution()
    assert expect == solution.findMedianSortedArrays(nums1, nums2)
