from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        results = set()
        repeats = set()
        for i in self._iterate(A, B):
            if i in results:
                repeats.add(i)
            else:
                results.add(i)
        results.difference_update(repeats)
        return list(results)

    @staticmethod
    def _iterate(a: str, b: str) -> str:
        chars = []
        for i in (a, b):
            for char in i:
                if char == ' ':
                    if chars:
                        yield ''.join(chars)
                        chars.clear()
                else:
                    chars.append(char)
            if chars:
                yield ''.join(chars)
                chars.clear()


# Python 3
# Runtime: 32 ms, faster than 95.19% of Python3 online submissions
# for Uncommon Words from Two Sentences.
# Memory Usage: 13.8 MB, less than 9.09% of Python3 online submissions
# for Uncommon Words from Two Sentences.
