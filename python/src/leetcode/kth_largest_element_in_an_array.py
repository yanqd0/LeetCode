from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < 2 * k - 1:
            return self.helper(nums, len(nums) - k + 1, min)
        return self.helper(nums, k, max)

    @staticmethod
    def helper(nums: List[int], k: int, func):
        ret = None
        for _ in range(k):
            if ret is not None:
                nums.remove(ret)
            ret = func(nums)
        return ret
