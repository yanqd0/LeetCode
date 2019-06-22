"""
Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2index = {}
        for index, num in enumerate(nums):
            prev = num2index.get(target - num)
            if prev is None:
                num2index[num] = index
            else:
                return [prev, index]
        raise RuntimeError('No two sum solution!')


# Python 2
# Runtime: 32 ms, faster than 89.77% of Python online submissions for Two Sum.
# Memory Usage: 13.3 MB, less than 17.41% of Python online submissions
# for Two Sum.
#
# Python 3
# Runtime: 36 ms, faster than 93.97% of Python3 online submissions for Two Sum.
# Memory Usage: 14.5 MB, less than 26.27% of Python3 online submissions
# for Two Sum.
