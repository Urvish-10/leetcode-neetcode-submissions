class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        left = min(mn, mx)
        right = max(mn, mx)

        # 1. Remove both from left
        a = right + 1

        # 2. Remove both from right
        b = n - left

        # 3. Remove left one from left, right one from right
        c = (left + 1) + (n - right)

        return min(a, b, c)
