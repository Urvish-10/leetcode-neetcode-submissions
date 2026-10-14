class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        ans = []

        for _ in range(num):
            digit = min(sum, 9)
            ans.append(str(digit))
            sum -= digit

        return "".join(ans)