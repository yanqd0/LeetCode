package name.qidong.leetcode.test;

import name.qidong.leetcode.PalindromeNumber;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class PalindromeNumberTest {
    @ParameterizedTest
    @CsvFileSource(resources = "/palindrome_number.csv", numLinesToSkip = 1)
    void isPalindrome(int x, boolean expect) {
        PalindromeNumber solution = new PalindromeNumber();
        assertEquals(expect, solution.isPalindrome(x));
    }
}