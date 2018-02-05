package name.qidong.leetcode.test;

import name.qidong.leetcode.LongestSubstringWithoutRepeatingCharacters;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SuppressWarnings("SpellCheckingInspection")
class LongestSubstringWithoutRepeatingCharactersTest {
    private LongestSubstringWithoutRepeatingCharacters solution;

    @BeforeEach
    void setUp() {
        solution = new LongestSubstringWithoutRepeatingCharacters();
    }

    @ParameterizedTest(name = "{index} => input={0}, expect={1}")
    @CsvSource({
            "abcabcbb, 3",
            "bbbbb, 1",
            "pwwkew, 3",
            "c, 1",
            "au, 2",
            "aab, 2",
            "abba, 2",
            "ggububgvfk, 6",
            "cdd, 2",
            "'', 0"
    })
    void lengthOfLongestSubstring(String input, int expect) {
        assertEquals(expect, solution.lengthOfLongestSubstring(input));
    }
}
