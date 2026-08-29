from typing import List

class Solution:
    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:

        n = len(nums)

        # Sort by value, while remembering original index
        arr = sorted((value, index) for index, value in enumerate(nums))

        ans = [0] * n

        i = 0

        while i < n:
            j = i + 1

            # Find one connected group.
            # If adjacent sorted values differ by <= limit,
            # they can belong to the same group.
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            # Original indices belonging to this group
            indices = sorted(index for _, index in arr[i:j])

            # Values are already sorted because arr is sorted.
            # Put the smallest values at the smallest indices.
            for index, (value, _) in zip(indices, arr[i:j]):
                ans[index] = value

            i = j

        return ans