class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        dp0 = 1  # Best length ending at current number
        dp1 = 1  # Best length ending at current number + 1

        ans = 1

        for i in range(1, len(nums)):
            prev = nums[i - 1]
            curr = nums[i]

            diff = curr - prev

            if diff == 0:
                dp1 = dp0 + 1

            elif diff == 1:
                dp0 += 1
                dp1 += 1

            elif diff == 2:
                dp0 = dp1 + 1
                dp1 = 1

            else:
                dp0 = 1
                dp1 = 1

            ans = max(ans, dp0, dp1)

        return ans