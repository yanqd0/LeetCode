package name.qidong.leetcode.test;

import org.junit.Test;

import static name.qidong.leetcode.TwoSum.solution;
import static org.junit.Assert.*;


public class TwoSumTest {
    @Test
    public void testTwoSum() {
        int[] nums = new int[]{3, 2, 3};
        int target = 6;
        int[] expect = new int[]{0, 2};

        int[] result = solution(nums, target);
        assertArrayEquals(expect, result);
    }
}
