class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1

        x = n

        while x:
            x, digit = divmod(x, 10)

            digit_sum += digit
            digit_product *= digit

        return n % (digit_sum + digit_product) == 0
