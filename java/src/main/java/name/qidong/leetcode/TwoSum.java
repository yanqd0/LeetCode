package name.qidong.leetcode;

import java.util.*;

/**
 * Given an array of integers, return indices of the two numbers such that they add up to a specific
 * target.
 * <p>
 * You may assume that each input would have exactly one solution, and you may not use the same
 * element twice.
 * <p>
 * Example:
 * <p>
 * Given nums = [2, 7, 11, 15], target = 9,
 * <p>
 * Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
 *
 * @see <a href="https://leetcode.com/problems/two-sum/">Two Sum - LeetCode</a>
 */
public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            Integer index = map.get(target - nums[i]);
            if (index == null) {
                map.put(nums[i], i);
            } else {
                return new int[]{index, i};
            }
        }
        throw new IllegalArgumentException("No two sum solution!");
    }
}
