class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        from array import array

        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        size = m * n

        right = array('i', [-1]) * size
        down = array('i', [-1]) * size

        # Precompute destinations after all mirror reflections.
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                k = i * n + j

                if j + 1 < n:
                    if grid[i][j + 1] == 0:
                        right[k] = k + 1
                    else:
                        right[k] = down[k + 1]

                if i + 1 < m:
                    if grid[i + 1][j] == 0:
                        down[k] = k + n
                    else:
                        down[k] = right[k + n]

        # Count paths using DP.
        dp = array('i', [0]) * size
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                k = i * n + j

                if dp[k] == 0:
                    continue

                ways = dp[k]

                r = right[k]
                if r != -1:
                    dp[r] = (dp[r] + ways) % MOD

                d = down[k]
                if d != -1:
                    dp[d] = (dp[d] + ways) % MOD

        return dp[-1]