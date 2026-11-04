class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}

        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def add(self, i, delta):
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i

            def query(self, i):
                s = 0
                while i:
                    s += self.bit[i]
                    i -= i & -i
                return s

            def kth(self, k):
                idx = 0
                bit_mask = 1 << (self.n.bit_length() - 1)

                while bit_mask:
                    nxt = idx + bit_mask
                    if nxt <= self.n and self.bit[nxt] < k:
                        idx = nxt
                        k -= self.bit[nxt]
                    bit_mask >>= 1

                return idx + 1

        cnt = Fenwick(m)
        sm = Fenwick(m)

        total = 0

        def update(v, delta):
            nonlocal total
            r = rank[v]
            cnt.add(r, delta)
            sm.add(r, v * delta)
            total += v * delta

        def get_cost():
            mid_idx = cnt.kth((x + 1) // 2)
            median = vals[mid_idx - 1]

            left_count = cnt.query(mid_idx)
            left_sum = sm.query(mid_idx)

            right_count = x - left_count
            right_sum = total - left_sum

            return (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

        costs = []

        for i in range(x):
            update(nums[i], 1)

        costs.append(get_cost())

        for i in range(x, n):
            update(nums[i - x], -1)
            update(nums[i], 1)
            costs.append(get_cost())

        INF = float('inf')

        prev = [0] * (n + 1)

        for _ in range(k):
            cur = [INF] * (n + 1)

            for i in range(1, n + 1):
                cur[i] = cur[i - 1]

                if i >= x:
                    c = costs[i - x]
                    cur[i] = min(cur[i], prev[i - x] + c)

            prev = cur

        return prev[n]