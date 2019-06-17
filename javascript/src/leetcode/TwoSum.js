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
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const map = new Map();
  for (let i = 0; i < nums.length; ++i) {
    let j = map[nums[i]];
    if (j === undefined) {
      map[target - nums[i]] = i;
    } else {
      return [j, i];
    }
  }
  throw new Error('No two sum solution!');
};

/*
Runtime: 56 ms, faster than 93.56% of JavaScript online submissions for Two Sum.
Memory Usage: 34.5 MB, less than 82.58% of JavaScript online submissions for Two Sum.
*/

export { twoSum };
