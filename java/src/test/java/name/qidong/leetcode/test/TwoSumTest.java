package name.qidong.leetcode.test;

import name.qidong.leetcode.TwoSum;
import name.qidong.leetcode.test.util.String2int;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.converter.ConvertWith;
import org.junit.jupiter.params.provider.CsvFileSource;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.fail;

class TwoSumTest {
    private TwoSum solution = new TwoSum();

    @ParameterizedTest
    @CsvFileSource(resources = "/two_sum.csv", numLinesToSkip = 1)
    void twoSum(
            @ConvertWith(String2int.class) int[] nums,
            int target,
            @ConvertWith(String2int.class) int[] expect
    ) {
        assertArrayEquals(expect, solution.twoSum(nums, target));
    }

    @Test
    void twoSumError() {
        int[] nums = new int[]{3, 2, 3};
        int target = 7;

        try {
            solution.twoSum(nums, target);
            fail("IllegalArgumentException expected!");
        } catch (IllegalArgumentException e) {
            // pass
        }
    }
}
