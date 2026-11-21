class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26

        def dfs(node):
            c = ord(s[node]) - ord('a')
            prev = last[c]
            last[c] = node

            if prev != -1:
                new_parent[node] = prev

            for child in children[node]:
                dfs(child)

            last[c] = prev

        dfs(0)

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [1] * n

        def calc(node):
            for child in new_children[node]:
                calc(child)
                ans[node] += ans[child]

        calc(0)

        return ans