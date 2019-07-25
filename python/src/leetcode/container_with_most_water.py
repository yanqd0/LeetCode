"""
Given n non-negative integers a1, a2, ..., an ,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai)
and (i, 0).
Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case,
the max area of water (blue section) the container can contain is 49.
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                current = (right - left) * height[left]
                left += 1
            else:
                current = (right - left) * height[right]
                right -= 1
            if current > area:
                area = current
        return area


# Python 2
# Runtime: 100 ms, faster than 87.38% of Python online submissions
# for Container With Most Water.
# Memory Usage: 13 MB, less than 59.49% of Python online submissions
# for Container With Most Water.
#
# Python 3
# Runtime: 132 ms, faster than 94.68% of Python3 online submissions
# for Container With Most Water.
# Memory Usage: 15.4 MB, less than 5.03% of Python3 online submissions
# for Container With Most Water.
