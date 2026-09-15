class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        def is_pal(l: int, r: int) -> bool:  # inclusive bounds
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        ans = 0
        i = 0
        while i + k <= n:
            if is_pal(i, i + k - 1):
                ans += 1
                i += k
            elif i + k < n and is_pal(i, i + k):
                ans += 1
                i += k + 1
            else:
                i += 1
        return ans