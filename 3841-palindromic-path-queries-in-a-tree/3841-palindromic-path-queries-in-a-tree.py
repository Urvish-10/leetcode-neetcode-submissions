from typing import List


class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        val = [1 << (ord(c) - 97) for c in s]

        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        size = [1] * n
        pref = [0] * n          # XOR of masks from root to node (initial string)
        order = []

        # iterative DFS (preorder => subtrees are contiguous)
        stack = [0]
        up[0][0] = 0
        pref[0] = val[0]
        visited = [False] * n
        visited[0] = True
        while stack:
            node = stack.pop()
            tin[node] = len(order)
            order.append(node)
            for nxt in adj[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    up[0][nxt] = node
                    depth[nxt] = depth[node] + 1
                    pref[nxt] = pref[node] ^ val[nxt]
                    stack.append(nxt)

        for node in reversed(order):
            if node != 0:
                size[up[0][node]] += size[node]

        for k in range(1, LOG):
            prev, cur = up[k - 1], up[k]
            for i in range(n):
                cur[i] = prev[prev[i]]

        # Fenwick tree: range XOR update, point query
        bit = [0] * (n + 2)

        def bit_add(i: int, d: int) -> None:
            while i <= n:
                bit[i] ^= d
                i += i & -i

        def bit_query(i: int) -> int:
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r

        def get_p(x: int) -> int:
            return pref[x] ^ bit_query(tin[x] + 1)

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            k = 0
            while diff:
                if diff & 1:
                    a = up[k][a]
                diff >>= 1
                k += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return up[0][a]

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new = 1 << (ord(parts[2]) - 97)
                delta = val[u] ^ new
                if delta:
                    val[u] = new
                    l = tin[u] + 1
                    r = tin[u] + size[u] + 1   # position just after the subtree
                    bit_add(l, delta)
                    bit_add(r, delta)          # ignored automatically if r > n
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)
                mask = get_p(u) ^ get_p(v) ^ val[w]
                ans.append(mask & (mask - 1) == 0)
        return ans