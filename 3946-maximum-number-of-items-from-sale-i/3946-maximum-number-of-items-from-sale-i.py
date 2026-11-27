class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    bonus[i] += 1

        dp = [-10**9] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            price = items[i][1]
            b = bonus[i]

            new = dp[:]

            for money in range(price, budget + 1):
                new[money] = max(
                    new[money],
                    dp[money - price] + 1 + b,
                    new[money - price] + 1
                )

            dp = new

        return max(dp)