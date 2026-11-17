class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # proper divisors d (1 <= d < m) for every length m
        divs = [[] for _ in range(n + 1)]
        for d in range(1, n):
            for m in range(2 * d, n + 1, d):
                divs[m].append(d)

        # cost[i][j] = min changes to make s[i..j] a semi-palindrome
        # (length 1 is impossible -> INF)
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best = INF
                for d in divs[L]:
                    c = 0
                    step_count = L // d
                    for r in range(d):
                        lo = i + r
                        hi = lo + (step_count - 1) * d
                        while lo < hi:
                            if s[lo] != s[hi]:
                                c += 1
                            lo += d
                            hi -= d
                    if c < best:
                        best = c
                cost[i][j] = best

        # dp[p][j] = min cost splitting first j chars into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for j in range(2 * p, n + 1):
                best = INF
                for i in range(2 * (p - 1), j - 1):
                    if dp[p - 1][i] != INF and cost[i][j - 1] != INF:
                        v = dp[p - 1][i] + cost[i][j - 1]
                        if v < best:
                            best = v
                dp[p][j] = best

        return dp[k][n]