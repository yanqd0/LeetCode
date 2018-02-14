package name.qidong.leetcode.test;

import name.qidong.leetcode.LongestPalindromicSubstring;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class LongestPalindromicSubstringTest {
    private LongestPalindromicSubstring solution;

    @BeforeEach
    void setUp() {
        solution = new LongestPalindromicSubstring();
    }

    @SuppressWarnings("SpellCheckingInspection")
    @ParameterizedTest(name = "{index} => s={0}, expect={1}")
    @CsvSource({
            "'', ''",
            "'a', 'a'",
            "'abb', 'bb'",
            "'ccd', 'cc'",
            "'cbbd', 'bb'",
            "'aaaab', 'aaaa'",
            "'abbbb', 'bbbb'",
            "'babad', 'bab'",
            "'aaaaab', 'aaaaa'",
            "'abbbbb', 'bbbbb'",
            "'ababababccd', 'abababa'",
            "'abcdefgfedcba', 'abcdefgfedcba'",
            "'abcdefg', 'a'",
    })
    void longestPalindrome(String s, String expect) {
        assertEquals(expect, solution.longestPalindrome(s));
    }
}
