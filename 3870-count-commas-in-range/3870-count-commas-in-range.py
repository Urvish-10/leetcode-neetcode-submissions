class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            count += f"{i:,}".count(",")
        return count