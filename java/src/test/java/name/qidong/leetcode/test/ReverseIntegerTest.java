package name.qidong.leetcode.test;

import name.qidong.leetcode.ReverseInteger;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ReverseIntegerTest {
    @ParameterizedTest
    @CsvFileSource(resources = "/reverse_integer.csv", numLinesToSkip = 1)
    void reverse(int x, int expect) {
        ReverseInteger solution = new ReverseInteger();
        assertEquals(expect, solution.reverse(x));
    }
}