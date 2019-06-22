/**
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * <p>
 * Find the median of the two sorted arrays. The overall run time complexity should be O(log(m+n)).
 * <p>
 * Example 1:
 * <pre>
 * nums1 = [1, 3]
 * nums2 = [2]
 *
 * The median is 2.0
 * </pre>
 * Example 2:
 * <pre>
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 *
 * The median is (2 + 3)/2 = 2.5
 * </pre>
 *
 * @see <a href="https://leetcode.com/problems/median-of-two-sorted-arrays/">Median of Two Sorted
 * Arrays - LeetCode</a>
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  if (nums1.length > nums2.length) {
    [nums1, nums2] = [nums2, nums1];
  }

  const half = Math.floor((nums1.length + nums2.length + 1) / 2);
  let start = 0;
  let end = nums1.length;
  let index1, index2;
  do {
    index1 = Math.floor((start + end) / 2);
    index2 = half - index1;

    if (index1 > 0 && nums1[index1 - 1] > nums2[index2]) {
      end = index1 - 1;
    } else if (index1 < nums1.length && nums1[index1] < nums2[index2 - 1]) {
      start = index1 + 1;
    } else {
      break;
    }
  } while (start <= end);

  let left;
  if (index1 <= 0) {
    left = nums2[index2 - 1];
  } else if (index2 <= 0) {
    left = nums1[index1 - 1];
  } else {
    left = Math.max(nums1[index1 - 1], nums2[index2 - 1]);
  }

  if ((nums1.length + nums2.length) % 2 === 1) {
    return left;
  }

  let right;
  if (index1 >= nums1.length) {
    right = nums2[index2];
  } else if (index2 >= nums2.length) {
    right = nums1[index1];
  } else {
    right = Math.min(nums1[index1], nums2[index2]);
  }
  return (left + right) / 2;
};

/*
Runtime: 104 ms, faster than 94.97% of JavaScript online submissions
for Median of Two Sorted Arrays.
Memory Usage: 38.9 MB, less than 85.78% of JavaScript online submissions
for Median of Two Sorted Arrays.
*/

export default findMedianSortedArrays;
