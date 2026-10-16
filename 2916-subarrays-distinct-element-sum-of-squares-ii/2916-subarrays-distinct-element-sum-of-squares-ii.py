class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        sm = [0] * (4 * n)    # sum of d[j]
        sq = [0] * (4 * n)    # sum of d[j]^2
        lz = [0] * (4 * n)    # lazy add

        def apply(o, l, r, v):
            ln = r - l + 1
            sq[o] += 2 * v * sm[o] + v * v * ln
            sm[o] += v * ln
            lz[o] += v

        def push(o, l, r):
            if lz[o]:
                m = (l + r) // 2
                apply(2 * o, l, m, lz[o])
                apply(2 * o + 1, m + 1, r, lz[o])
                lz[o] = 0

        def update(o, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(o, l, r, 1)
                return
            push(o, l, r)
            m = (l + r) // 2
            if ql <= m:
                update(2 * o, l, m, ql, qr)
            if qr > m:
                update(2 * o + 1, m + 1, r, ql, qr)
            sm[o] = sm[2 * o] + sm[2 * o + 1]
            sq[o] = sq[2 * o] + sq[2 * o + 1]

        last = {}
        ans = 0
        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, n - 1, p + 1, i)
            last[x] = i
            # positions > i are still 0, so the root's sq is the sum over [0, i]
            ans = (ans + sq[1]) % MOD
        return ans