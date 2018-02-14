package name.qidong.leetcode;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ZigZagConversionTest {
    private ZigZagConversion solution;

    @BeforeEach
    void setUp() {
        solution = new ZigZagConversion();
    }

    @SuppressWarnings("SpellCheckingInspection")
    @ParameterizedTest(name = "{index} => s={0}, expect={1}")
    @CsvSource({
            "'', 0, ''",
            "'', 1, ''",
            "'ABC', 0, 'ABC'",
            "'ABC', 1, 'ABC'",
            "'PAYPALISHIRING', 0, 'PAYPALISHIRING'",
            "'PAYPALISHIRING', 1, 'PAYPALISHIRING'",
            "'PAYPALISHIRING', 2, 'PYAIHRNAPLSIIG'",
            "'PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'",
            "'abcdefghijklmn', 4, 'agmbfhlnceikdj'",
            "'abcdefghijklmn', 5, 'aibhjcgkdflnem'",
            "'abcdefghijklmno', 5, 'aibhjcgkodflnem'",
            "'abcdefghijklmnop', 5, 'aibhjpcgkodflnem'",
            "'abcde', 5, 'abcde'",
    })
    void convert(String s, int numRows, String expect) {
        assertEquals(expect, solution.convert(s, numRows));
    }
}