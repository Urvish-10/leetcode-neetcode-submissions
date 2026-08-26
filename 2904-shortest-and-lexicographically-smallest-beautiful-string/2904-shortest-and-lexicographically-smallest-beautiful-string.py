class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # Too many 1s -> shrink from left
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # Remove leading zeros.
            # This gives the shortest substring ending at `right`
            # that contains exactly k ones.
            while ones == k and s[left] == '0':
                left += 1

            if ones == k:
                curr = s[left:right + 1]

                if not ans or len(curr) < len(ans):
                    ans = curr
                elif len(curr) == len(ans) and curr < ans:
                    ans = curr

        return ans
