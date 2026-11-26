class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        turn = 0

        while n >= remove:
            n -= remove
            remove -= 1
            turn += 1

        return turn % 2 == 1