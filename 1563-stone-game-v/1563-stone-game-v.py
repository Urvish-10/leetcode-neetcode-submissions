class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dp(i, j):
            if i == j:
                return 0

            ans = 0
            left = 0
            total = prefix[j + 1] - prefix[i]

            for k in range(i, j):
                left += stoneValue[k]
                right = total - left

                if left < right:
                    # Right is discarded, keep left.
                    ans = max(ans, left + dp(i, k))

                elif left > right:
                    # Left is discarded, keep right.
                    ans = max(ans, right + dp(k + 1, j))

                else:
                    # Equal sums: Alice chooses either side.
                    ans = max(
                        ans,
                        left + dp(i, k),
                        right + dp(k + 1, j)
                    )

            return ans

        return dp(0, len(stoneValue) - 1)