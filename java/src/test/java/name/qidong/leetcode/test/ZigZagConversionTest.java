package name.qidong.leetcode.test;

import name.qidong.leetcode.ZigZagConversion;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ZigZagConversionTest {
    @ParameterizedTest
    @CsvFileSource(resources = "/zigzag_conversion.csv", numLinesToSkip = 1)
    void convert(String s, int numRows, String expect) {
        ZigZagConversion solution = new ZigZagConversion();
        assertEquals(expect, solution.convert(s, numRows));
    }
}