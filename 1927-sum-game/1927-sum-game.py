class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # If the number of '?' is odd, Alice can always
        # make the sums unequal.
        if (left_q + right_q) % 2 == 1:
            return True

        # Difference between known sums.
        diff = left_sum - right_sum

        # Bob can compensate for the difference only if
        # the '?' counts and required compensation match.
        return diff * 2 != 9 * (right_q - left_q)