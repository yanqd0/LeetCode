from pytest import mark

from leetcode.spiral_matrix_iii import Solution

from . import read_csv


@mark.parametrize('inputs, expect', read_csv(__file__, parser=eval))
def test_two_sum(inputs, expect):
    assert expect == Solution().spiralMatrixIII(*inputs)
