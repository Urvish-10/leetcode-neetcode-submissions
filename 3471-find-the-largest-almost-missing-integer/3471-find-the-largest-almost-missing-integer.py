class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Case 1: every element forms its own subarray
        if k == 1:
            freq = Counter(nums)
            ans = -1

            for num in nums:
                if freq[num] == 1:
                    ans = max(ans, num)

            return ans

        # Case 2: only one subarray exists
        if k == n:
            return max(nums)

        # Case 3: 1 < k < n
        freq = Counter(nums)

        ans = -1

        if freq[nums[0]] == 1:
            ans = max(ans, nums[0])

        if freq[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans