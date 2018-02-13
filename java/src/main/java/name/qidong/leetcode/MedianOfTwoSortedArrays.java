package name.qidong.leetcode;

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
 */
public class MedianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        int start = 0, end = nums1.length;
        int half = (nums1.length + nums2.length + 1) / 2;
        while (start <= end) {
            int index1 = (start + end) / 2;
            int index2 = half - index1;

            if (index1 > 0 && nums1[index1 - 1] > nums2[index2]) {
                end = index1 - 1;
            } else if (index1 < nums1.length && nums1[index1] < nums2[index2 - 1]) {
                start = index1 + 1;
            } else {
                int left;
                if (index1 <= 0) {
                    left = nums2[index2 - 1];
                } else if (index2 <= 0) {
                    left = nums1[index1 - 1];
                } else {
                    left = Math.max(nums1[index1 - 1], nums2[index2 - 1]);
                }

                if ((nums1.length + nums2.length) % 2 == 1) {
                    return left;
                }

                int right;
                if (index1 >= nums1.length) {
                    right = nums2[index2];
                } else if (index2 >= nums2.length) {
                    right = nums1[index1];
                } else {
                    right = Math.min(nums1[index1], nums2[index2]);
                }
                return (left + right) / 2.0;
            }
        }
        throw new RuntimeException("No answer!");
    }
}
