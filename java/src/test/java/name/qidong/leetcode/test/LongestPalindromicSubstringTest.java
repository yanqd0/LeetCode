package name.qidong.leetcode.test;

import name.qidong.leetcode.LongestPalindromicSubstring;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class LongestPalindromicSubstringTest {
    @ParameterizedTest
    @CsvFileSource(resources = "/longest_palindromic_substring.csv", numLinesToSkip = 1)
    void longestPalindrome(String s, String expect) {
        LongestPalindromicSubstring solution = new LongestPalindromicSubstring();
        assertEquals(expect, solution.longestPalindrome(s));
    }
}
