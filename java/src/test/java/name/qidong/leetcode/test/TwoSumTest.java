package name.qidong.leetcode.test;

import name.qidong.leetcode.*;
import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.*;

class TwoSumTest {
    private TwoSum solution = new TwoSum();

    @Test
    void twoSum() {
        int[] nums = new int[]{3, 2, 3};
        int target = 6;
        int[] expect = new int[]{0, 2};

        int[] result = solution.twoSum(nums, target);
        assertArrayEquals(expect, result);
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