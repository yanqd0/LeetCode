from pytest import mark

from leetcode.median_of_two_sorted_arrays import Solution

from . import read_csv


@mark.parametrize('nums1, nums2, expect', read_csv(__file__, parser=eval))
def test_find_median_sorted_arrays(nums1, nums2, expect):
    solution = Solution()
    assert expect == solution.findMedianSortedArrays(nums1, nums2)
