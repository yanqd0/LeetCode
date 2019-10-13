from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums) // 2 + len(nums) % 2
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

    def a_fail_solution(self, nums: List[int]) -> None:
        length = len(nums)
        for i in range(length):
            map_i = self.map_index(i, length)
            bigger = map_i
            for j in range(i + 1, length):
                map_j = self.map_index(j, length)
                if nums[bigger] < nums[map_j]:
                    bigger = map_j
            nums[map_i], nums[bigger] = nums[bigger], nums[map_i]

    @staticmethod
    def kth_max_value(nums: List[int], left: int, right: int, k: int) -> int:
        """
        Find the kth max value like quick sort.

        The k should be [0, 1, 2, 3 ...].
        """
        if left >= right:
            return nums[left]

        low, high = left, right
        median = nums[high]
        while low < high:
            while low < high and nums[low] > median:
                low += 1
            nums[high] = nums[low]
            while low < high and nums[high] <= median:
                high -= 1
            nums[low] = nums[high]
        nums[high] = median

        if high > k:
            return Solution.kth_max_value(nums, left, high - 1, k)
        if high < k:
            return Solution.kth_max_value(nums, high + 1, right, k)
        return median

    @staticmethod
    def map_index(i: int, length: int) -> int:
        """
        map a to b

        a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        b = [1, 3, 5, 7, 0, 2, 4, 6, 8]

        a = [0, 1, 2, 3, 4, 5, 6, 7]
        b = [1, 3, 5, 7, 0, 2, 4, 6]

        It is an order from max to min in a wiggle way.
        """
        j = i * 2 + 1
        if j < length:
            return j
        return j - length + length % 2 - 1

    @staticmethod
    def median_index(i: int) -> int:
        """
        The median index should be [0, -1, 1, -2, 2, -3 ...].

        The sign should be [1, -1, 1, -1 ...].
        The num should be [0, 1, 1, 2, 2, 3, 3 ...].
        """
        sign = 1 - (i % 2) * 2
        num = i // 2 + i % 2
        return sign * num

    @classmethod
    def place_same_median(cls, nums, median):
        """
        Put repeated median values around the mapped mid.
        """
        length = len(nums)
        mid = length // 2

        i = 0
        inside = mid + cls.median_index(i)
        map_i = cls.map_index(inside, length)
        for j in range(length):
            while i < length and nums[map_i] == median:
                i += 1
                inside = mid + cls.median_index(i)
                map_i = cls.map_index(inside, length)

            if i + j >= length - 1:
                break

            outside = mid + cls.median_index(length - 1 - j)
            map_o = cls.map_index(outside, length)
            if nums[map_o] == median:
                nums[map_i], nums[map_o] = nums[map_o], nums[map_i]

    @classmethod
    def quick_sort_once_with_median(cls, nums, median):
        length = len(nums)
        left, mid, right = 0, length // 2, length - 1
        map_l = cls.map_index(left, length)
        map_r = cls.map_index(right, length)

        for i in range(mid):
            map_i = cls.map_index(i, length)
            while right > mid and nums[map_r] < median:
                right -= 1
                map_r = cls.map_index(right, length)
            if right == mid:
                break
            if nums[map_i] < nums[map_r]:
                nums[map_i], nums[map_r] = nums[map_r], nums[map_i]
        for j in range(length - 1, mid, -1):
            map_j = cls.map_index(j, length)
            while left < mid and nums[map_l] > median:
                left += 1
                map_l = cls.map_index(left, length)
            if left == mid:
                break
            if nums[map_l] < nums[map_j]:
                nums[map_j], nums[map_l] = nums[map_l], nums[map_j]
