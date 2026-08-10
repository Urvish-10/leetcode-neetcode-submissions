class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            j = 1

            while j * j <= i:
                # If removing j^2 leaves the opponent
                # in a losing position, current player wins.
                if not dp[i - j * j]:
                    dp[i] = True
                    break

                j += 1

        return dp[n]