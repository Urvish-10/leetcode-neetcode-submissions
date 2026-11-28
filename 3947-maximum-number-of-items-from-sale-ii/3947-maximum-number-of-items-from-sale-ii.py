class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        for f, _ in items:
            freq[f] += 1

        total = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f]:
                total[f] = sum(freq[f::f])

        cheapest = min(p for _, p in items)
        res = 0

        for f, p in sorted(items, key=lambda x: x[1]):
            if p >= 2 * cheapest:
                break
            k = min(total[f] - 1, budget // p)
            res += 2 * k
            budget -= k * p

        return res + budget // cheapest