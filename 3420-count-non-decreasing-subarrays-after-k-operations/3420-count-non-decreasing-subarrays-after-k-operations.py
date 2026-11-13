from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        ans = 0
        cost = 0
        j = n - 1

        for i in range(n - 1, -1, -1):
            num = nums[i]

            while dq and nums[dq[-1]] < num:
                l = dq.pop()
                r = dq[-1] if dq else j + 1
                cost += (r - l) * (num - nums[l])

            dq.append(i)

            while cost > k:
                cost -= nums[dq[0]] - nums[j]

                if dq[0] == j:
                    dq.popleft()

                j -= 1

            ans += j - i + 1

        return ans