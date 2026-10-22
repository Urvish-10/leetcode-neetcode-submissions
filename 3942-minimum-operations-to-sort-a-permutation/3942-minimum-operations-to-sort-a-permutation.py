class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        inc = all(nums[i] == (nums[0] + i) % n for i in range(n))
        if inc:
            k = nums[0]
            ans = min(ans, (n - k) % n, k + 2)

        dec = all(nums[i] == (nums[0] - i) % n for i in range(n))
        if dec:
            k = (n - 1 - nums[0]) % n
            ans = min(ans, 1 + min(k, (n - k) % n))

        return ans if ans != float('inf') else -1