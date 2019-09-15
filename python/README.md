# leetcode.py

[![Code style: yapf](https://img.shields.io/badge/code%20style-yapf-blue)](https://github.com/google/yapf)

## Problems

1. No.1 [Two Sum](https://leetcode.com/problems/two-sum) | [两数之和 ](https://leetcode-cn.com/problems/two-sum)
    - Code: [two_sum.py](./src/leetcode/two_sum.py)
    - Test: [test_two_sum.py](./tests/test_two_sum.py)
1. No.2 [Add Two Numbers](https://leetcode.com/problems/add-two-numbers) | [两数相加](https://leetcode-cn.com/problems/add-two-numbers)
    - Code: [add_two_numbers.py](./src/leetcode/add_two_numbers.py)
    - Test: [test_add_two_numbers.py](./tests/test_add_two_numbers.py)
1. No.3 [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | [无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters)
    - Code: [longest_substring_without_repeating_characters.py](./src/leetcode/longest_substring_without_repeating_characters.py)
    - Test: [test_longest_substring_without_repeating_characters.py](./tests/test_longest_substring_without_repeating_characters.py)
1. No.4 [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) | [寻找两个有序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays)
    - Code: [median_of_two_sorted_arrays.py](./src/leetcode/median_of_two_sorted_arrays.py)
    - Test: [test_median_of_two_sorted_arrays.py](./tests/test_median_of_two_sorted_arrays.py)
1. No.5 [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring) | [最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring)
    - Code: [longest_palindromic_substring.py](./src/leetcode/longest_palindromic_substring.py)
    - Test: [test_longest_palindromic_substring.py](./tests/test_longest_palindromic_substring.py)
1. No.6 [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion) | [Z 字形变换](https://leetcode-cn.com/problems/zigzag-conversion)
    - Code: [zigzag_conversion.py](./src/leetcode/zigzag_conversion.py)
    - Test: [test_zigzag_conversion.py](./tests/test_zigzag_conversion.py)
1. No.7 [Reverse Integer](https://leetcode.com/problems/reverse-integer) | [整数反转](https://leetcode-cn.com/problems/reverse-integer)
    - Code: [reverse_integer.py](./src/leetcode/reverse_integer.py)
    - Test: [test_reverse_integer.py](./tests/test_reverse_integer.py)
1. No.8 [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi) | [字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi)
    - Code: [string_to_integer_atoi.py](./src/leetcode/string_to_integer_atoi.py)
    - Test: [test_string_to_integer_atoi.py](./tests/test_string_to_integer_atoi.py)
1. No.9 [Palindrome Number](https://leetcode.com/problems/palindrome-number) | [回文数](https://leetcode-cn.com/problems/palindrome-number)
    - Code: [palindrome_number.py](./src/leetcode/palindrome_number.py)
    - Test: [test_palindrome_number.py](./tests/test_palindrome_number.py)
1. No.10 [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) | [正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching)
    - Code: [regular_expression_matching.py](./src/leetcode/regular_expression_matching.py)
    - Test: [test_regular_expression_matching.py](./tests/test_regular_expression_matching.py)
1. No.11 [Container With Most Water](https://leetcode.com/problems/container-with-most-water) | [盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water)
    - Code: [container_with_most_water.py](./src/leetcode/container_with_most_water.py)
    - Test: [test_container_with_most_water.py](./tests/test_container_with_most_water.py)
1. No.27 [Remove Element](https://leetcode.com/problems/remove-element) | [移除元素](https://leetcode-cn.com/problems/remove-element)
    - Code: [remove_element.py](./src/leetcode/remove_element.py)
    - Test: [test_remove_element.py](./tests/test_remove_element.py)
1. No.31 [Next Permutation](https://leetcode.com/problems/next-permutation/) | [下一个排列](https://leetcode-cn.com/problems/next-permutation/)
    - Code: [next_permutation.py](./src/leetcode/next_permutation.py)
    - Test: [test_next_permutation.py](./tests/test_next_permutation.py)
1. No.48 [Rotate Image](https://leetcode.com/problems/rotate-image/) | [旋转图像](https://leetcode-cn.com/problems/rotate-image/)
    - Code: [rotate_image.py](./src/leetcode/rotate_image.py)
    - Test: [test_rotate_image.py](./tests/test_rotate_image.py)
1. No.56 [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | [合并区间](https://leetcode-cn.com/problems/merge-intervals/)
    - Code: [merge_intervals.py](./src/leetcode/merge_intervals.py)
    - Test: [merge_intervals.py](./tests/merge_intervals.py)
1. No.151 [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | [翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)
    - Code: [reverse_words_in_a_string.py](./src/leetcode/reverse_words_in_a_string.py)
    - Test: [reverse_words_in_a_string.py](./tests/reverse_words_in_a_string.py)


## Setup

```sh
pip install -r requirements.txt
pip install -e .
```

## Develop

Add new solutions as modules in `src/leetcode/`, and their tests in `tests`.

## Test

Run tests:

```sh
pytest
# or
./setup.py test
```

Generate coverage reports:

```sh
coverage html
```

Then open `htmlcov/index.html` in a browser.
