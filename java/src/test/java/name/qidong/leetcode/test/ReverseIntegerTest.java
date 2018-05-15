package name.qidong.leetcode.test;

import name.qidong.leetcode.ReverseInteger;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ReverseIntegerTest {
    private ReverseInteger solution;

    @BeforeEach
    void setUp() {
        solution = new ReverseInteger();
    }

    @ParameterizedTest(name = "{index} => s={0}, expect={1}")
    @CsvSource({
            "1, 1",
            "120, 21",
            "123, 321",
            "-123, -321",
            "1534236469, 0",
            "2147483642, 0",
            "-2147483648, 0",
    })
    void reverse(int x, int expect) {
        assertEquals(expect, solution.reverse(x));
    }
}