"""
Implement next permutation, which rearranges numbers into
the lexicographically next greater permutation of numbers.

If such arrangement is not possible,
it must rearrange it as the lowest possible order
(ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples.
Inputs are in the left-hand column and its corresponding outputs
are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in reversed(range(len(nums))):
            if i > 0 and nums[i - 1] < nums[i]:
                for j in reversed(range(len(nums))):
                    if nums[j] > nums[i - 1]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        self.reverse(nums, i)
                        break
                break
        else:
            self.reverse(nums)

    @staticmethod
    def reverse(nums: List[int], i=0):
        length = len(nums)
        for j in range((length - i) // 2):
            left = i + j
            right = length - 1 - j
            nums[left], nums[right] = nums[right], nums[left]


# Python 3
# Runtime: 40 ms, faster than 99.42% of Python3 online submissions
# for Next Permutation.
# Memory Usage: 13.9 MB, less than 5.56% of Python3 online submissions
# for Next Permutation.
