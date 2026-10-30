import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        heap = [(0, 0, 1)]

        while heap:
            cost, node, count = heapq.heappop(heap)

            if cost > dist[node][count]:
                continue

            if node == n - 1:
                return cost

            for neighbor, weight in graph[node]:
                next_count = count + 1 if labels[node] == labels[neighbor] else 1

                if next_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[neighbor][next_count]:
                    dist[neighbor][next_count] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor, next_count))

        return -1