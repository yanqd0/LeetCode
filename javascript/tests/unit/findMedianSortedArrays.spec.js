import { readCases } from './utils';
import findMedianSortedArrays from '../../src/leetcode/findMedianSortedArrays';

const CASES = readCases('median_of_two_sorted_arrays.csv');

describe('findMedianSortedArrays.js', () => {
  test.each(CASES)('nums1=%s, nums2=%s, expect=%s', (nums1, nums2, expected) => {
    expect(expected).toEqual(findMedianSortedArrays(nums1, nums2));
  });
});
