class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
            
        seen = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            char = s[right]
            seen[char] = seen.get(char, 0) + 1

            while seen[char] > 2:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
            
        return ans