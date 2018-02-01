package name.qidong.leetcode.test;

import name.qidong.leetcode.TwoSum;
import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.fail;


public class TwoSumTest {
    private TwoSum solution = new TwoSum();

    @Test
    public void testTwoSum() {
        int[] nums = new int[]{3, 2, 3};
        int target = 6;
        int[] expect = new int[]{0, 2};

        int[] result = solution.twoSum(nums, target);
        assertArrayEquals(expect, result);
    }

    @Test
    public void testTwoSumWithError() {
        int[] nums = new int[]{3, 2, 3};
        int target = 7;

        try {
            solution.twoSum(nums, target);
            fail();
        } catch (IllegalArgumentException e) {
            // pass
        }
    }
}
