from pytest import mark

from leetcode.rotate_image import Solution

from . import read_csv


@mark.parametrize('matrix, expect', read_csv(__file__, parser=eval))
def test_two_sum(matrix, expect):
    assert Solution().rotate(matrix) is None
    assert matrix == expect
