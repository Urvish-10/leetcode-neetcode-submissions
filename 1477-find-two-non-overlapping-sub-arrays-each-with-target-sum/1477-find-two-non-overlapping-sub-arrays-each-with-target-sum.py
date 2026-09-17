from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        # best[i] = shortest valid subarray entirely
        # within arr[0 : i]
        INF = float("inf")
        best = [INF] * (n + 1)

        left = 0
        current_sum = 0
        answer = INF

        for right in range(n):
            current_sum += arr[right]

            # Shrink the window if sum exceeds target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            # Current window has sum == target
            if current_sum == target:
                length = right - left + 1

                # best[left] contains a valid subarray
                # that ends before the current window
                if best[left] != INF:
                    answer = min(answer, best[left] + length)

                # Update best prefix minimum
                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        return -1 if answer == INF else answer