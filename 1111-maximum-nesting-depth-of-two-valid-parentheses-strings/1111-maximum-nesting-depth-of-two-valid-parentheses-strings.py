class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth = 0
        ans = []

        for ch in seq:
            if ch == "(":
                depth += 1
                ans.append(depth & 1)
            else:
                ans.append(depth & 1)
                depth -= 1

        return ans
