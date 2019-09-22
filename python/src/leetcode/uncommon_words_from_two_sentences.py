from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        repeats = set()
        a_set = set()
        for i in A.split():
            if i in a_set:
                repeats.add(i)
            else:
                a_set.add(i)
        b_set = set()
        for i in B.split():
            if i in b_set:
                repeats.add(i)
            else:
                b_set.add(i)

        diff = a_set.symmetric_difference(b_set)
        return list(diff.difference(repeats))


# Python 3
# Runtime: 36 ms, faster than 80.46% of Python3 online submissions
# for Uncommon Words from Two Sentences.
# Memory Usage: 14 MB, less than 9.09% of Python3 online submissions
# for Uncommon Words from Two Sentences.
