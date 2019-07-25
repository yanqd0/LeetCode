/**
 * Given n non-negative integers a1, a2, ..., an ,
 * where each represents a point at coordinate (i, ai).
 * n vertical lines are drawn such that the two endpoints of line i is at (i, ai)
 * and (i, 0).
 * Find two lines, which together with x-axis forms a container,
 * such that the container contains the most water.
 *
 * Note: You may not slant the container and n is at least 2.
 *
 * https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
 *
 * The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
 * In this case,
 * the max area of water (blue section) the container can contain is 49.
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let max = 0;
  let left = 0;
  let right = height.length - 1;
  while (left < right) {
    let area = 0;
    if (height[left] < height[right]) {
      area = height[left] * (right - left);
      ++left;
    } else {
      area = height[right] * (right - left);
      --right;
    }
    if (area > max) {
      max = area;
    }
  }
  return max;
};

/*
Runtime: 60 ms, faster than 78.13% of JavaScript online submissions for Container With Most Water.
Memory Usage: 35.6 MB, less than 52.82% of JavaScript online submissions for Container With Most Water.
*/

export default maxArea;
