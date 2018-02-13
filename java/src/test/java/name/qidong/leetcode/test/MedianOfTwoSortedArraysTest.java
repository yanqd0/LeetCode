package name.qidong.leetcode.test;


import name.qidong.leetcode.MedianOfTwoSortedArrays;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.extension.ParameterContext;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.converter.ArgumentConversionException;
import org.junit.jupiter.params.converter.ArgumentConverter;
import org.junit.jupiter.params.converter.ConvertWith;
import org.junit.jupiter.params.provider.CsvSource;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MedianOfTwoSortedArraysTest {
    private MedianOfTwoSortedArrays solution;

    @BeforeEach
    void setUp() {
        solution = new MedianOfTwoSortedArrays();
    }

    @ParameterizedTest(name = "{index} => nums1={0}, nums2={1}, expect={2}")
    @CsvSource({
            "[], [1], 1.0",
            "[2], [], 2.0",
            "[2], '[1, 3, 4]', 2.5",
            "'[1, 2, 4]', [3], 2.5",
            "[3], '[1, 2]', 2.0",
            "[2], '[1, 3, 4, 5]', 3.0",
            "[4], '[1, 2, 3, 5]', 3.0",
            "'[1, 4]', '[2, 3, 5, 6, 7]', 4.0",
            "'[1, 3]', [2], 2.0",
            "'[1, 2]', '[3, 4]', 2.5",
            "'[1, 3]', '[2, 4]', 2.5",
            "'[2, 3]', '[1, 4]', 2.5",
            "[1], [3], 2.0",
            "[1], '[1, 2, 3, 4]', 2.0",
            "[9], '[1, 2, 3, 4]', 3.0",
            "'[1, 2, 3, 4, 5, 6]', '[1, 2]', 2.5",
            "'[1, 2, 3, 4, 5, 6]', '[3, 4]', 3.5",
            "'[1, 2, 3, 4, 5, 6]', '[5, 6]', 4.5",
            "'[1, 2, 3, 4, 5, 6]', '[3, 4, 5, 6, 7, 8, 9]', 5.0",
            "'[1, 2, 3, 4, 8, 9]', '[3, 4, 5, 6, 7, 8, 9]', 5.0",
    })
    void findMedianSortedArrays(
            @ConvertWith(String2int.class) int[] nums1,
            @ConvertWith(String2int.class) int[] nums2,
            double expect
    ) {
        assertEquals(expect, solution.findMedianSortedArrays(nums1, nums2));
    }

    static class String2int implements ArgumentConverter {
        @Override
        public Object convert(Object source, ParameterContext context)
                throws ArgumentConversionException {
            try {
                String str = (String) source;
                str = str.trim().substring(1, str.length() - 1).trim();
                if (str.isEmpty()) return new int[]{};
                if (!str.contains(",")) return new int[]{Integer.parseInt(str)};
                return Arrays.stream(str.split(","))
                             .map(String::trim)
                             .mapToInt(Integer::parseInt).toArray();
            } catch (ClassCastException e) {
                throw new ArgumentConversionException("The source is not a String", e);
            } catch (NumberFormatException e) {
                throw new ArgumentConversionException("Some content in source is not int", e);
            }
        }
    }
}
