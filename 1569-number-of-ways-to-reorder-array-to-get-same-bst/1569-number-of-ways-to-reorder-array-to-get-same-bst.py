from math import comb
from functools import lru_cache

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = tuple(x for x in arr[1:] if x < root)
            right = tuple(x for x in arr[1:] if x > root)

            return (
                comb(len(arr) - 1, len(left))
                * dfs(left)
                * dfs(right)
            ) % MOD

        return (dfs(tuple(nums)) - 1) % MOD