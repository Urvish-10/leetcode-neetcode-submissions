from functools import cache
from itertools import pairwise
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2:
            return False

        if grid[0][0] == ")" or grid[m - 1][n - 1] == "(":
            return False

        @cache
        def dfs(i, j, balance):
            balance += 1 if grid[i][j] == "(" else -1

            if balance < 0:
                return False

            # Not enough cells remaining to close all '('
            if balance > m - i + n - j:
                return False

            if i == m - 1 and j == n - 1:
                return balance == 0

            for di, dj in ((1, 0), (0, 1)):
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n:
                    if dfs(ni, nj, balance):
                        return True

            return False

        return dfs(0, 0, 0)
