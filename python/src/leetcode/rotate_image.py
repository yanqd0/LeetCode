"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
00 -> 03
01 -> 13
02 -> 23
03 -> 33

10 -> 02
11 -> 12
12 -> 22
13 -> 32

20 -> 01
21 -> 11
22 -> 21
23 -> 31

30 -> 00
31 -> 10
32 -> 20
33 -> 30
"""

from typing import List, Tuple


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length // 2):
            for j in range(0, length - i - i - 1):
                x0, y0 = i, i + j
                x1, y1 = self.next(x0, y0, length)
                x2, y2 = self.next(x1, y1, length)
                x3, y3 = self.next(x2, y2, length)
                (
                    matrix[x0][y0],
                    matrix[x1][y1],
                    matrix[x2][y2],
                    matrix[x3][y3],
                ) = (
                    matrix[x3][y3],
                    matrix[x0][y0],
                    matrix[x1][y1],
                    matrix[x2][y2],
                )

    @staticmethod
    def next(i: int, j: int, length: int) -> Tuple[int, int]:
        return j, length - i - 1


# Python3
# Runtime: 44 ms, faster than 50.99% of Python3 online submissions
# for Rotate Image.
# Memory Usage: 13.6 MB, less than 6.25% of Python3 online submissions
# for Rotate Image.
