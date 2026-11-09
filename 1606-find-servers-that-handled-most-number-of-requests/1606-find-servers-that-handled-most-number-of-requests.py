class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = list(range(k))
        busy = []
        count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, server = heappop(busy)
                insort(available, server)

            if not available:
                continue

            pos = bisect_left(available, i % k)

            if pos == len(available):
                pos = 0

            server = available.pop(pos)
            count[server] += 1

            heappush(busy, (start + duration, server))

        max_count = max(count)

        return [i for i, c in enumerate(count) if c == max_count]