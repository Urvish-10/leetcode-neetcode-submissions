class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Convert stones into prefix sums in-place
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # dp[n-1] = sum of all stones
        best = stones[-1]

        # dp[i] = max(dp[i+1], prefix[i] - dp[i+1])
        for i in range(n - 2, 0, -1):
            best = max(best, stones[i] - best)

        return best