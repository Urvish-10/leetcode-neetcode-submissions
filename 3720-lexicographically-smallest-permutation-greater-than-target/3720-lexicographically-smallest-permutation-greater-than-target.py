class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26

        for ch in s:
            count[ord(ch) - 97] += 1

        # Match target as far as possible using available letters of s
        matched = 0
        while matched < n:
            c = ord(target[matched]) - 97
            if count[c] == 0:
                break
            count[c] -= 1
            matched += 1

        # Try to increase at the rightmost possible position first
        for pos in range(min(matched, n - 1), -1, -1):
            if pos < matched:
                # undo the match at this position so it's available again
                count[ord(target[pos]) - 97] += 1

            target_c = ord(target[pos]) - 97
            for c in range(target_c + 1, 26):
                if count[c] > 0:
                    count[c] -= 1
                    # build result: prefix same as target, then c, then sorted remainder
                    result = list(target[:pos])
                    result.append(chr(c + 97))
                    for x in range(26):
                        result.append(chr(x + 97) * count[x])
                    count[c] += 1  # restore (not strictly needed, loop ends)
                    return "".join(result)

        return ""