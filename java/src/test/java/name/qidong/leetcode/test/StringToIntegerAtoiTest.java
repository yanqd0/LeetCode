package name.qidong.leetcode.test;

import name.qidong.leetcode.StringToIntegerAtoi;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

import static org.junit.jupiter.api.Assertions.assertEquals;


class StringToIntegerAtoiTest {

    @ParameterizedTest
    @CsvFileSource(resources = "/string_to_integer_atoi.csv", numLinesToSkip = 1)
    void myAtoi(String input, int expect) {
        StringToIntegerAtoi solution = new StringToIntegerAtoi();
        assertEquals(expect, solution.myAtoi(input));
    }
}