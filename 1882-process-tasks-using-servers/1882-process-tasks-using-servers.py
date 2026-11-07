
import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        # Available servers: (weight, index)
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        # Busy servers: (free_time, weight, index)
        busy = []

        ans = []
        current_time = 0

        for i, duration in enumerate(tasks):

            # Current task arrives at second i
            current_time = max(current_time, i)

            # Release all servers that are free
            while busy and busy[0][0] <= current_time:
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # If no server is available, wait
            if not available:

                current_time = busy[0][0]

                # Release all servers becoming free
                # at this time
                while busy and busy[0][0] <= current_time:
                    free_time, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Select the best available server
            weight, idx = heapq.heappop(available)

            ans.append(idx)

            # Mark server as busy
            heapq.heappush(
                busy,
                (current_time + duration, weight, idx)
            )

        return ans
