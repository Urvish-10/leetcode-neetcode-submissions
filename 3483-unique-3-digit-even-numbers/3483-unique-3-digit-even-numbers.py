class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10
        for d in digits:
            count[d] += 1

        ans = set()

        def backtrack(num: int, length: int):
            if length == 3:
                if num % 2 == 0:
                    ans.add(num)
                return

            for d in range(10):
                if count[d] == 0:
                    continue

                # Hundreds digit cannot be zero.
                if length == 0 and d == 0:
                    continue

                count[d] -= 1
                backtrack(num * 10 + d, length + 1)
                count[d] += 1

        backtrack(0, 0)
        return len(ans)