package name.qidong.leetcode.test;


import name.qidong.leetcode.MedianOfTwoSortedArrays;
import name.qidong.leetcode.test.util.String2IntegerArray;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.converter.ConvertWith;
import org.junit.jupiter.params.provider.CsvFileSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MedianOfTwoSortedArraysTest {
    @ParameterizedTest
    @CsvFileSource(resources = "/median_of_two_sorted_arrays.csv", numLinesToSkip = 1)
    void findMedianSortedArrays(
            @ConvertWith(String2IntegerArray.class) int[] nums1,
            @ConvertWith(String2IntegerArray.class) int[] nums2,
            double expect
    ) {
        MedianOfTwoSortedArrays solution = new MedianOfTwoSortedArrays();
        assertEquals(expect, solution.findMedianSortedArrays(nums1, nums2));
    }
}
