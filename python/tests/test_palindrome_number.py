from pytest import mark

from leetcode.palindrome_number import Solution

from . import read_csv


@mark.parametrize('x, expect', read_csv(__file__, parser=eval))
def test_find_median_sorted_arrays(x, expect):
    solution = Solution()
    assert expect == solution.isPalindrome(x)
