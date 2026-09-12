from typing import List
from functools import lru_cache
from bisect import bisect_right


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        arr = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        n = len(arr)
        starts = [x[0] for x in arr]

        @lru_cache(None)
        def dp(i, k):
            # (maximum score, lexicographically smallest indices)
            if i == n or k == 0:
                return (0, ())

            # Option 1: Skip current interval.
            skip_score, skip_indices = dp(i + 1, k)

            # Option 2: Take current interval.
            l, r, w, idx = arr[i]
            j = bisect_right(starts, r)

            next_score, next_indices = dp(j, k - 1)

            take_score = w + next_score
            take_indices = tuple(sorted((idx,) + next_indices))

            # Choose the better score.
            if take_score > skip_score:
                return take_score, take_indices

            if take_score < skip_score:
                return skip_score, skip_indices

            # Equal score: lexicographically smaller indices.
            return skip_score, min(take_indices, skip_indices)

        return list(dp(0, 4)[1])