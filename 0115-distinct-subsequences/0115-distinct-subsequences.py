class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[j] = number of ways to form t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1

        for ch in s:
            # Traverse backward so each character is used once
            for j in range(n - 1, -1, -1):
                if ch == t[j]:
                    dp[j + 1] += dp[j]

        return dp[n]
