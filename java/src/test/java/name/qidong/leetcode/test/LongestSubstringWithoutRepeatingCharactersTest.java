package name.qidong.leetcode.test;

import name.qidong.leetcode.LongestSubstringWithoutRepeatingCharacters;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SuppressWarnings("SpellCheckingInspection")
class LongestSubstringWithoutRepeatingCharactersTest {
    @ParameterizedTest
    @CsvFileSource(
            resources = "/longest_substring_without_repeating_characters.csv",
            numLinesToSkip = 1
    )
    void lengthOfLongestSubstring(String input, int expect) {
        LongestSubstringWithoutRepeatingCharacters solution =
                new LongestSubstringWithoutRepeatingCharacters();
        assertEquals(expect, solution.lengthOfLongestSubstring(input));
    }
}
