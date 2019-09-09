"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019.
Please reset to default code definition to get new method signature.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in intervals:
            mergables = set()
            for index, j in enumerate(merged):
                if Solution.mergable(i, j):
                    mergables.add(index)
            if mergables:
                i = Solution.merge_with(i, mergables, merged)
                merged = Solution.remove_mergables(merged, mergables)
            merged.append(i)
        return merged

    @staticmethod
    def mergable(x: List[int], y: List[int]) -> bool:
        return y[0] <= x[0] <= y[1] or x[0] <= y[0] <= x[1]

    @staticmethod
    def merge_with(
        one: List[int],
        indexes: List[int],
        merged: List[List[int]],
    ) -> List[int]:
        left, right = zip(*(merged[i] for i in indexes))
        one[0] = min(one[0], *left)
        one[1] = max(one[1], *right)
        return one

    @staticmethod
    def remove_mergables(
        merged: List[List[int]],
        mergables: List[int],
    ) -> List[List[int]]:
        return [v for k, v in enumerate(merged) if k not in mergables]
