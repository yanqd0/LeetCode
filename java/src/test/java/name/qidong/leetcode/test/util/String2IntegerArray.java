package name.qidong.leetcode.test.util;

import org.junit.jupiter.api.extension.ParameterContext;
import org.junit.jupiter.params.converter.ArgumentConversionException;
import org.junit.jupiter.params.converter.ArgumentConverter;

import java.util.Arrays;

public class String2IntegerArray implements ArgumentConverter {
    @Override
    public Object convert(Object source, ParameterContext context)
            throws ArgumentConversionException {
        try {
            String str = (String) source;
            str = str.trim().substring(1, str.length() - 1).trim();
            if (str.isEmpty()) return new int[]{};
            if (!str.contains(",")) return new int[]{Integer.parseInt(str)};
            return Arrays.stream(str.split(","))
                         .map(String::trim)
                         .mapToInt(Integer::parseInt).toArray();
        } catch (ClassCastException e) {
            throw new ArgumentConversionException("The source is not a String", e);
        } catch (NumberFormatException e) {
            throw new ArgumentConversionException("Some content in source is not int", e);
        }
    }
}
