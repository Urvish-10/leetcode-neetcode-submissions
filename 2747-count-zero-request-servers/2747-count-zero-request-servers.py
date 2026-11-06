from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        ans = [0] * len(queries)

        active = defaultdict(int)
        left = right = 0
        count = 0

        for q, idx in sorted_queries:
            while right < len(logs) and logs[right][1] <= q:
                server, time = logs[right]
                if active[server] == 0:
                    count += 1
                active[server] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server, time = logs[left]
                active[server] -= 1
                if active[server] == 0:
                    count -= 1
                left += 1

            ans[idx] = n - count

        return ans