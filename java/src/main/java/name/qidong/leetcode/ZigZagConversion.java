package name.qidong.leetcode;

/**
 * The string <code>"PAYPALISHIRING"</code> is written in a zigzag pattern on a given number of rows
 * like this: (you may want to display this pattern in a fixed font for better legibility)
 * <p>
 * <pre><code>
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * </code></pre>
 * <p>
 * And then read line by line: <code>"PAHNAPLSIIGYIR"</code>
 * <p>
 * Write the code that will take a string and make this conversion given a number of rows:
 * <p>
 * <pre><code>
 * string convert(string text, int nRows);
 * </code></pre>
 * <p>
 * <code>convert("PAYPALISHIRING", 3)</code> should return <code>"PAHNAPLSIIGYIR"</code>.
 *
 * @see <a href="https://leetcode.com/problems/zigzag-conversion/description/">ZigZag Conversion -
 * LeetCode</a>
 */
@SuppressWarnings("SpellCheckingInspection")
public class ZigZagConversion {
    public String convert(String s, int numRows) {
        if (numRows <= 1 || s.length() <= numRows) {
            return s;
        }

        StringBuilder[] strings = new StringBuilder[numRows];
        for (int i = 0; i < numRows; ++i) {
            strings[i] = new StringBuilder();
        }

        int row = 0;
        int step = 1;
        for (char ch : s.toCharArray()) {
            strings[row].append(ch);

            if (row == 0) {
                step = 1;
            } else if (row == numRows - 1) {
                step = -1;
            }
            row += step;
        }

        StringBuilder result = new StringBuilder();
        for (StringBuilder builder : strings) {
            result.append(builder);
        }
        return result.toString();
    }
}
