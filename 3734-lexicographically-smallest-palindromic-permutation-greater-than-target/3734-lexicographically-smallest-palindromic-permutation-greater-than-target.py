from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = Counter(s)

        # A palindrome can have at most one character
        # with an odd frequency.
        odd = [ch for ch in cnt if cnt[ch] % 2]

        if len(odd) > 1:
            return ""

        # Character in the middle (only for odd length)
        mid = odd[0] if odd else ""

        # Characters available for the left half
        half_cnt = [0] * 26
        for ch, c in cnt.items():
            half_cnt[ord(ch) - ord('a')] = c // 2

        half_len = n // 2
        path = []

        def build_max_palindrome():
            """
            Given the current prefix in path, construct the
            LARGEST possible palindrome using the remaining
            characters.

            If even this largest palindrome <= target,
            no completion can work.
            """
            left = path[:]

            # Put remaining characters in descending order
            for i in range(25, -1, -1):
                if half_cnt[i]:
                    left.extend([chr(i + ord('a'))] * half_cnt[i])

            left = ''.join(left)

            return left + mid + left[::-1]

        # Greedily construct the smallest possible left half.
        for _ in range(half_len):

            for c in range(26):
                if half_cnt[c] == 0:
                    continue

                ch = chr(c + ord('a'))

                # Try this character
                half_cnt[c] -= 1
                path.append(ch)

                # Is there ANY completion that can beat target?
                if build_max_palindrome() > target:
                    # Yes -> this is the smallest feasible choice.
                    break

                # No -> undo and try the next character.
                path.pop()
                half_cnt[c] += 1

            else:
                # No character can be placed at this position.
                return ""

        # Construct final palindrome
        left = ''.join(path)
        ans = left + mid + left[::-1]

        return ans if ans > target else ""