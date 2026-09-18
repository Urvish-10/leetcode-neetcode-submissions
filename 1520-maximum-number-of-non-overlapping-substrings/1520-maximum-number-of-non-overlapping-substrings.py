class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence of every character
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')

            first[idx] = min(first[idx], i)
            last[idx] = i

        def get_interval(start):
            ch_idx = ord(s[start]) - ord('a')

            left = start
            right = last[ch_idx]

            i = left

            while i <= right:
                idx = ord(s[i]) - ord('a')

                # This character started before our substring.
                # Therefore the substring cannot be valid.
                if first[idx] < left:
                    return -1, -1

                # We must include all occurrences of this character.
                right = max(right, last[idx])

                i += 1

            return left, right

        result = []

        for i in range(n):

            # Only start from first occurrence of a character
            if first[ord(s[i]) - ord('a')] != i:
                continue

            left, right = get_interval(i)

            if left == -1:
                continue

            if not result:
                result.append((left, right))

            else:
                prev_left, prev_right = result[-1]

                if left > prev_right:
                    # Completely non-overlapping
                    result.append((left, right))

                else:
                    # Current interval is nested inside previous.
                    result[-1] = (left, right)

        return [s[left:right + 1] for left, right in result]