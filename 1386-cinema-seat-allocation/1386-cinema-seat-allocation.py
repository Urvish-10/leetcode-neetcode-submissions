class Solution:
    def maxNumberOfFamilies(
        self, n: int, reservedSeats: List[List[int]]
    ) -> int:

        rows = defaultdict(int)

        for row, seat in reservedSeats:
            rows[row] |= 1 << (seat - 1)

        ans = (n - len(rows)) * 2

        # seats 2-5
        LEFT = 0b00000011110

        # seats 4-7
        MIDDLE = 0b0001111000

        # seats 6-9
        RIGHT = 0b0111100000

        for reserved in rows.values():
            left = (reserved & LEFT) == 0
            middle = (reserved & MIDDLE) == 0
            right = (reserved & RIGHT) == 0

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans