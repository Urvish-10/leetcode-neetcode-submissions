class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]

        for x in stones:
            count[x % 3] += 1

        # count[0] is even
        if count[0] % 2 == 0:
            return min(count[1], count[2]) > 0

        # count[0] is odd
        return abs(count[1] - count[2]) > 2