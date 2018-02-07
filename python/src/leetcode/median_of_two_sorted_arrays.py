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
"""


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr1, arr2 = SpecialArray(nums1), SpecialArray(nums2)

        if not nums1:
            return arr2.median
        if not nums2:
            return arr1.median

        if arr1.medians[0] > arr2.medians[1]:
            arr1, arr2 = arr2, arr1

        step = len(arr1) // 2 if len(arr1) < len(arr2) else len(arr2) // 2
        while True:
            if len(arr1) == 1:
                print('hello')
                return arr2.calc_median(arr1.median)
            elif len(arr2) == 1:
                return arr1.calc_median(arr2.median)
            if arr1.close_to(arr2):
                medians = sorted(arr1.medians + arr2.medians)
                return (medians[1] + medians[2]) / 2

            if arr1.medians[1] < arr2.medians[0]:
                arr1.start += step
                arr2.end -= step
            else:
                arr1.start -= step
                arr2.end += step
            step = (step + 1) // 2


class SpecialArray:
    def __init__(self, nums):
        self.nums = nums
        self.start = 0
        self.end = len(nums) - 1

    def __len__(self):
        return self.end - self.start + 1

    @property
    def left(self):
        return (self.start + self.end) // 2

    @property
    def right(self):
        return (self.start + self.end + 1) // 2

    @property
    def medians(self):
        return self.nums[self.left], self.nums[self.right]

    @property
    def median(self):
        return sum(self.medians) / 2

    def calc_median(self, median):
        med_left, med_right = self.medians
        if med_left != med_right and med_left > median:
            return med_left
        elif med_left != med_right and med_right < median:
            return med_right
        elif med_left > median:
            index = self.left - 1
            if index < 0 or self.nums[index] < median:
                value = median
            else:
                value = self.nums[index]
            return (value + med_left) / 2
        elif med_right < median:
            index = self.left + 1
            if index < 0 or self.nums[index] > median:
                value = median
            else:
                value = self.nums[index]
            return (value + med_left) / 2
        else:
            return median

    def close_to(self, other):
        self_left, self_right = self.medians
        other_left, other_right = other.medians
        return self_left <= other_right and self_right >= other_left
