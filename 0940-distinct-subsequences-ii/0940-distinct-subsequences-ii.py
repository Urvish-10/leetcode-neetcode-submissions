class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # dp[i] = number of distinct subsequences
        # ending with character chr(ord('a') + i)
        dp = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            # All existing distinct subsequences can be
            # extended by ch, plus ch itself.
            dp[i] = sum(dp) + 1

            dp[i] %= MOD

        return sum(dp) % MOD
