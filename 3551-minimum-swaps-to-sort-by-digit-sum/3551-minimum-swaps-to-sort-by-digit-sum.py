class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(map(int, str(n)))

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {num: i for i, num in enumerate(sorted_nums)}

        n = len(nums)
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_size += 1

            swaps += max(0, cycle_size - 1)

        return swaps