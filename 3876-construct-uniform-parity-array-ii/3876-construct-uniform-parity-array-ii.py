class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Smallest odd number
        min_odd = min((x for x in nums1 if x % 2 == 1), default=None)

        # No odd numbers -> all numbers are even
        if min_odd is None:
            return True

        # Every even number must be greater than the smallest odd
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True