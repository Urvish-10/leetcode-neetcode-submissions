class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # return comb(n + k - 1, 2 * k) % (10**9 + 7)
        MOD = 10**9 + 7
        dp = [1] * n              # j = 0: one way (no segments)
        for j in range(1, k + 1):
            new = [0] * n
            prefix = dp[0]        # sum of dp[p][j-1] for p < i
            for i in range(1, n):
                new[i] = (new[i - 1] + prefix) % MOD
                prefix = (prefix + dp[i]) % MOD
            dp = new
        return dp[n - 1]