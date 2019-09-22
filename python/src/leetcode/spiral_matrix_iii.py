from typing import List


class Solution:
    def spiralMatrixIII(
            self,
            R: int,
            C: int,
            r0: int,
            c0: int,
    ) -> List[List[int]]:  # yapf: disable
        origin = [r0, c0]
        ret = [origin]
        coords = origin.copy()
        count = R * C - 1
        for i in range(1, max(R, C) * 2):
            sign = 1 if i % 2 else -1
            for j in range(2):
                for _ in range(i):
                    coords[1 - j] += sign
                    if 0 <= coords[0] < R and 0 <= coords[1] < C:
                        ret.append(coords.copy())

                        count -= 1
                        if count == 0:
                            return ret
        return ret


# Python 3
# Runtime: 148 ms, faster than 30.32% of Python3 online submissions
# for Spiral Matrix III.
# Memory Usage: 15 MB, less than 50.00% of Python3 online submissions
# for Spiral Matrix III.
