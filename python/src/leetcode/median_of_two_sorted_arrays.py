"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
from typing import List


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        start, end = 0, len(nums1)
        half = (len(nums1) + len(nums2) + 1) // 2
        while start <= end:
            index1 = (start + end) // 2
            index2 = half - index1

            if index1 > 0 and nums1[index1 - 1] > nums2[index2]:
                end = index1 - 1
            elif index1 < len(nums1) and nums1[index1] < nums2[index2 - 1]:
                start = index1 + 1
            else:
                break

        if index1 <= 0:
            left = nums2[index2 - 1]
        elif index2 <= 0:
            left = nums1[index1 - 1]
        else:
            left = max(nums1[index1 - 1], nums2[index2 - 1])
        if (len(nums1) + len(nums2)) % 2 == 1:
            return left

        if index1 >= len(nums1):
            right = nums2[index2]
        elif index2 >= len(nums2):
            right = nums1[index1]
        else:
            right = min(nums1[index1], nums2[index2])
        return (left + right) / 2


# Python 2
# Runtime: 68 ms, faster than 92.27% of Python online submissions
# for Median of Two Sorted Arrays.
# Memory Usage: 11.9 MB, less than 47.98% of Python online submissions
# for Median of Two Sorted Arrays.
#
# # Python 3
# Runtime: 56 ms, faster than 86.76% of Python3 online submissions
# for Median of Two Sorted Arrays.
# Memory Usage: 13.4 MB, less than 47.79% of Python3 online submissions
# for Median of Two Sorted Arrays.
