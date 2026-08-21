class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        # Count how many distinct valid amounts are <= x
        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                curr_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        curr_lcm = lcm(curr_lcm, coins[i])

                        # No multiple of this LCM can be <= x
                        if curr_lcm > x:
                            break

                if bits % 2 == 1:
                    # Add odd-sized subsets
                    total += x // curr_lcm
                else:
                    # Subtract even-sized subsets
                    total -= x // curr_lcm

            return total

        # The answer cannot exceed min(coins) * k
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left