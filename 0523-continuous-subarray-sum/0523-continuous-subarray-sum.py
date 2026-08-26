class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        remainder_index = {0:-1}

        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in remainder_index:
                if i - remainder_index[remainder] >= 2:
                    return True
            else:
                remainder_index[remainder] = i

        return False