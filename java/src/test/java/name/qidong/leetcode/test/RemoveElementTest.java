package name.qidong.leetcode.test;

import name.qidong.leetcode.RemoveElement;
import name.qidong.leetcode.test.util.String2IntegerArray;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.converter.ConvertWith;
import org.junit.jupiter.params.provider.CsvFileSource;

import static org.junit.jupiter.api.Assertions.assertEquals;


class RemoveElementTest {
    @ParameterizedTest
    @CsvFileSource(resources = "/remove_element.csv", numLinesToSkip = 1)
    void removeElement(
            @ConvertWith(String2IntegerArray.class) int[] nums,
            int val,
            int expect,
            @ConvertWith(String2IntegerArray.class) int[] new_nums
    ) {
        RemoveElement solution = new RemoveElement();
        assertEquals(expect, solution.removeElement(nums, val));
        for (int i = 0; i < expect; ++i) {
            assertEquals(new_nums[i], nums[i]);
        }
    }
}
